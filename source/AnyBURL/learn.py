import sys
sys.path.append('.')
from algorithm.path_sampler import PathSampler
from structure.rule import Rule
import time

class Learn(object):
  
  '''/**
	* Number of maximal attempts to create body grounding. Every partial body grounding is counted.
	*/'''
  trial_size = 1000000

  '''/**
	* Used for restricting the number of samples drawn for computing scores as confidence.
	*/'''
  sample_size = 1000
  '''/**
	 * The time that is reserved for one batch in milliseconds. Each second batch is 
	 * used for mining cyclic/acyclic rules. 
	 */'''
  batch_time = 500
  '''/**
	 * The threshold for the number of correctly prediction within the given training set.
	 */'''
  threshold_correct_predictions = 5

  '''/**
	 * The threshold for the confidences.
	 */'''
  threshold_confidence = 0.05

  def __init__(self, train_path='../../datasets/FB15k-237/test.txt'):
    self.triple_set = TripleSet()
    self.triple_set.read_triples(train_path)
    self.rule_size = 0

  def train(self):
    print('* read {} triples'.format(len(self.triple_set.triples)))
    path_counter = 0
    path_sampler = PathSampler(self.triple_set)
    all_useful_rules = []
    batch_rules = 0
    all_useful_rules.append(set([]))
    batch_start_time = time.time()
    batch_previously_found_rules = 0
    while (True):
      current_time = time.time()
      if currentTime - batch_start_time > Learn.batch_time:
        break
      path_counter += 1
      useful_rules = all_useful_rules[0]
      p = path_sampler.sample_path(self.rule_size + 2, False)
      if p is not None and p.is_valid():
        pr = Rule(p)
        rules = pr.get_generalizations(False)
        for rule in rules:
          if rule.is_trivial():
            continue
          batch_rules += 1
          if rule not in useful_rules:
            rule.compute_scores(self.triple_set)
            if rule.gconfidence >= threshold_confidence and  rule.correctly_predicted >= threshold_correct_predictions:
              batch_previously_found_rules += 1
							# if (r.isXYRule()) batchNewUsefulCyclicRules++;
							# else batchNewUsefulAcyclicRules++;
              useful_rules.add(rule)
            else:
              batch_previously_found_rules += 1
              ## if (r.isXYRule()) batchPreviouslyFoundCyclicRules++;
              ## else batchPreviouslyFoundAcyclicRules++;
					