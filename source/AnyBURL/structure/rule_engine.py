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
            else:
              break
      
      k_tail_candidates,k_head_candidates = {}, {}
      k_tail_tree.get_as_linked_map(k_tail_candidates)
      k_head_tree.get_as_linked_map(k_head_candidates)

      top_k_tail_candidates = self.__sort_by_value(k_tail_candidates, k)
      top_k_head_candidates = self.__sort_by_value(k_head_candidates, k)

      self.__write_top_k_candidates()


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

  # to do: implement heap
  def __sort_by_value(self, candidates, k):
    heap = []
    for key, val in candidates.items():
      priority = -1 * val
      entry = (priority, (key, val))
      if len(heap) < k:
        heapq.heappush(heap, entry)
      else:
        is_push = False
        min_priority = min(heap)
        max_priority = max(heap)
        if priority < min_priority:
          heapq.heappush(heap, entry)
          is_push = True
        elif priority < max_priority:
          heapq.heappush(heap, entry)
          is_push = True
        # delete element out of top k
        if is_push:
          for index, (p, (key, val)) in enumerate(heap):
            if p ==  max(heap):
              del heap[index]
              break
          heapq.heapify(heap)
    sort_heap = sorted(heap, key=lambda item: item[0], reverse=True)
    res = {}
    for index, (p, (key, val)) in enumerate(sort_heap):
      res[key] = val
    return res

  def __write_top_k_candidates(self, output=sys.stdout):
    print('hello ', output)
        