from apply_config import ApplyConfig
from data.triple_set import TripleSet
from structure.score_tree import ScoreTree
import time
import heapq
import sys

class RuleEngine(object):

  combination_rule_id = 1
  epsilon = 1e-4

  def __init__(self):
    pass

  def apply_rules_arx(self, rules, training_set, test_set, validation_set, k):
    print('* applying rules')
    relation_to_rules = self.create_ordered_rule_index(rules)
    print('* set up index structure covering rules for {} different relations'.format(len(relation_to_rules)))
    filter_set = TripleSet()
    filter_set.add_triple_set(training_set)
    filter_set.add_triple_set(test_set)
    filter_set.add_triple_set(validation_set)
    print('* constructed filter set with {} triples'.format(len(filter_set.triples)))
    if len(filter_set.triples) == 0:
      print('WARNING: using empty filter set!')
    # prepare the data structures used a s cache for question that are reoccuring
    head_candidate_cache, tail_candidate_cache = {},{}
    # start iterating over the test cases
    counter ,current_time, start_time = 0, 0, time.time()

    ScoreTree.lower_bound = k
    ScoreTree.upper_bound = ScoreTree.lower_bound
    ScoreTree.epsilon = RuleEngine.epsilon
    f = open('test.txt', 'a')
    f_log = open('log.txt', 'w+')
    i = 0
    for triple in test_set.triples:
      if counter % 50 == 0:
        print('* (# {} ) trying to guess the tail/head of {}'.format(counter, triple))
        current_time = time.time()
        print('Elapsed (s) = {}'.format(int(current_time - start_time) // 1000))
        # 8 seconds per 1000 triples
      counter += 1
      relation = triple.relation
      head = triple.head
      tail = triple.tail
      tail_question, head_question = (relation, head), (relation, tail)
      k_tail_tree = ScoreTree()
      k_head_tree = ScoreTree()

      if relation in relation_to_rules:
        relevant_rules = relation_to_rules.get(relation)
        # print('* ( {} ) trying to guess the tail/head of {}'.format(relevant_rules[0], relation))
        if tail_question not in tail_candidate_cache:
          for rule in relevant_rules:
            if not k_tail_tree.fine():
              tail_candidates = rule.compute_tail_results(head, training_set)
              f_tail_candidates = self.__get_filtered_entities(filter_set, test_set, triple, tail_candidates, True)
              k_tail_tree.add_values(rule.get_applied_confidence(), f_tail_candidates)
            else:
              break

        if head_question not in head_candidate_cache:
          for rule in relevant_rules:
            if not k_head_tree.fine():
              head_candidates = rule.compute_head_results(tail, training_set)
              f_head_candidates = self.__get_filtered_entities(filter_set, test_set, triple, head_candidates, False)
              k_head_tree.add_values(rule.get_applied_confidence(), f_tail_candidates)
              if i < 100:
            else:
              break
        i += 1
      
      k_tail_candidates,k_head_candidates = {}, {}
      k_tail_tree.get_as_linked_map(k_tail_candidates)
      k_head_tree.get_as_linked_map(k_head_candidates)
      # print(k_tail_candidates, k_head_candidates)
      top_k_tail_candidates = self.__sort_by_value(k_tail_candidates, k)
      top_k_head_candidates = self.__sort_by_value(k_head_candidates, k)

      
      self.__write_top_k_candidates(triple, test_set, top_k_tail_candidates, top_k_head_candidates, f)
    
    
    f.close()

  def create_ordered_rule_index(self, rules):
    relation_to_rules = {}
    while len(rules) > 0:
      rule = rules.pop()
      relation = rule.get_target_relation()
      if relation not in relation_to_rules:
        relation_to_rules[relation] = []
      relation_to_rules[relation].append(rule)
    
    for value in relation_to_rules.values():
      value.sort(key=lambda v: v.correctly_predicted / (v.predicted + ApplyConfig.unseen_nagative_example))
    
    return relation_to_rules
  
  def __get_filtered_entities(self, filter_set, test_set, triple, candidate_entities, tail_not_head):
    filtered_entities = set()
    for entity in candidate_entities:
      if not tail_not_head:
        if not filter_set.is_true(entity, triple.relation, triple.tail):
          filtered_entities.add(entity)
        if test_set.is_true(entity, triple.relation, triple.tail):
          if entity == triple.head:
            filtered_entities.add(entity)
      else:
        if not filter_set.is_true(triple.head, triple.relation, entity):
          filtered_entities.add(entity)
        if test_set.is_true(triple.head, triple.relation, entity):
          if entity == triple.tail:
            filtered_entities.add(entity)
    
    return filtered_entities

  # to do: implement heap
  def __sort_by_value(self, candidates, k):
    heap = []
    
    for key, val in candidates.items():
      priority = -1 * val
      entry = (priority, (key, val))
      heapq.heappush(heap, entry)
      
    res = {}
    i = 0
    while i < k and len(heap):
      (_, (key, val)) = heapq.heappop(heap)
      res[key] = val
      i += 1
    return res

  def __write_top_k_candidates(self, triple, test_set, k_tail_candidates, top_k_head_candidates, output=sys.stdout):
    print('{}'.format(triple), file=output)
    print('Heads: ', file=output)
    for key, val in k_tail_candidates.items():
      if triple.head == key or not test_set.is_true(key, triple.relation, triple.tail):
        print('{}\t{}'.format(key.strip(), val), end='\t', file=output)
    print('\n', file=output)
    print('tails: ', file=output)
    for key, val in top_k_head_candidates.items():
      if triple.tail == key or not test_set.is_true(triple.head, triple.relation, key):
        print('{}\t{}\t'.format(key.strip(), val),  end='\t', file=output)
    print('\n', file=output)
    output.flush()