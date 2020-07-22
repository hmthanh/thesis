from config.config_yaml import Config
from data.triple_set import TripleSet
from eval.result_set import ResultSet
from eval.hits_atk import HitsAtK

class Evaluation(object):

  def __init__(self):
    cfg = Config()
    self.config = cfg.load_eval_config()
  
  def eval(self):
    training_set, validation_set, test_set = TripleSet(), TripleSet(), TripleSet()
    training_set.read_triples(self.config['path_training'])
    validation_set.read_triples(self.config['path_valid'])
    test_set.read_triples(self.config['path_test'])
    result_set = ResultSet(self.config['path_prediction'], self.config['path_prediction'])
    hitsAtK = HitsAtK()
    hitsAtK.filter_sets.append(training_set)
    hitsAtK.filter_sets.append(validation_set)
    hitsAtK.filter_sets.append(test_set)
    self.__compute_scores(result_set, test_set, hitsAtK)
  
  def __compute_scores(self, result_set, gold, hitsAtK):
    for triple in gold:
      cand1 = result_set.get_head_candidates(triple)
      hitsAtK.evaluate_head(cand1, t)
      cand2 = result_set.get_tail_candidates(triple)
      hitsAtK.evaluate_tail(cand2, t)