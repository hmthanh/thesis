from algorithm.path_sampler import PathSampler
from structure.rule import Rule
from data.triple_set import TripleSet
from learn_config import ConfigParameters
import time

class Learn(object):

  def __init__(self, train_path='../../datasets/FB15k-237/test.txt'):
    self.triple_set = TripleSet()
    self.triple_set.read_triples(train_path)
    self.rule_size = 0
    self.mine_cyclic_not_acyclic = False
    self.rule_size_cyclic = 0
    self.rule_size_acyclic = 0

  def train(self):
    print('* read {} triples'.format(len(self.triple_set.triples)))
    path_counter = 0
    path_sampler = PathSampler(self.triple_set)

    all_useful_rules = []
    all_useful_rules.append(set([]))
    start_time = time.time()

    while True:
      useful_rules = all_useful_rules[self.rule_size]
      this_time = time.time()
      elapsed_seconds = (this_time - start_time)
      if elapsed_seconds > 700:
        break

      batch_previously_found_rules = 0
      batch_rules = 0
      batch_new_useful_rules = 1
      self.rule_size = self.rule_size_acyclic
      if self.mine_cyclic_not_acyclic:
        self.rule_size = self.rule_size_cyclic
      batch_start_time = time.time()
      while True:
        current_time = time.time()
        if current_time - batch_start_time > ConfigParameters.batch_time:
          break
        path_counter += 1
        
        p = path_sampler.sample_path(self.rule_size + 2, self.mine_cyclic_not_acyclic)
        if p is not None and p.is_valid():
          pr = Rule()
          pr.init_from_path(p)
          rules = pr.get_generalizations(self.mine_cyclic_not_acyclic)
          for rule in rules:
            if rule.is_trivial():
              continue
            batch_rules += 1
            if rule not in useful_rules:
              rule.compute_scores(self.triple_set)
              if rule.confidence >= ConfigParameters.threshold_confidence and  rule.correctly_predicted >= ConfigParameters.threshold_correct_predictions:
                batch_new_useful_rules += 1
                useful_rules.add(rule)
            else:
              batch_previously_found_rules += 1
      
      current_coverage = batch_previously_found_rules / (batch_new_useful_rules + batch_previously_found_rules)
      print('>>> ~~~~~~~~~~~~~~~~~~current_coverage~~~~~~~~~~~~~~~~~~~~~~~~~~ ', current_coverage)
      if current_coverage > ConfigParameters.saturation: #and batch_previously_found_rules > 1
        self.rule_size += 1
        if self.mine_cyclic_not_acyclic:
          self.rule_size_cyclic = self.rule_size
        else:
          self.rule_size_acyclic = self.rule_size
        print('>>> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print('>>> INCREASING RULE SIZE OF rule_size_cyclic RULE TO ', (self.rule_size + 1))
        print(">>> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('increasing rule size of rule_size_acyclic rules to ', (self.rule_size + 1) , ' after ' , (start_time -  time.time() // 1000) , 's')
        all_useful_rules.append(set([]))
      self.mine_cyclic_not_acyclic = self.mine_cyclic_not_acyclic
      if self.mine_cyclic_not_acyclic and self.rule_size_cyclic + 1 > ConfigParameters.max_length_cylic:
        self.mine_cyclic_not_acyclic = False

    for rule_set in  all_useful_rules:
      print('================== done learning ====================, len useful_rules = {}'.format(len(rule_set)))
      i = 0
      for rule in rule_set:
        if i % 500 == 0:
          print(rule.confidence)
        i += 1
					