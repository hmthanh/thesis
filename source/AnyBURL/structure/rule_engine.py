from apply_config import ApplyConfig
from data.triple_set import TripleSet
from score_tree import ScoreTree
import time

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
      tail_question, head_question = {}. {}
      tail_question[relation] = head
      head_question[relation] = tail
      k_tail_tree = ScoreTree()
      k_head_tree = ScoreTree()

      if relation in relation_to_rules:
        relevant_rules = relation_to_rules.get(relation)
        if relevant_rules not in tail_candidate_cache:
          pass
        if relevant_rules not in head_candidate_cache:
          pass
    pass

  def create_ordered_rule_index(self, rules):
    relation_to_rules = {}
    while len(rules) > 0:
      rule = rules.pop()
      relation = rule.get_target_relation()
      if relation not in relation_to_rules:
        relation_to_rules[relation] = []
      relation_to_rules[relation].append(rule)
    
    for value in relation_to_rules.values():
      value.sort(key=lambda v: v.correctly_predicted / v.predicted + ApplyConfig.unseen_nagative_example)
    
    return relation_to_rules