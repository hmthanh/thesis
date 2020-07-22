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
    print('training_set')
    training_set.read_triples(self.config['path_training'])
    print('validation_set')
    validation_set.read_triples(self.config['path_valid'])
    print('test_set')
    test_set.read_triples(self.config['path_test'])
    print('read result_set')
    result_set = ResultSet(self.config['path_prediction'], self.config['path_prediction'])
    print('result_set {}'.format(len(result_set.results)))
    hitsAtK = HitsAtK()
    hitsAtK.filter_sets.append(training_set)
    hitsAtK.filter_sets.append(validation_set)
    hitsAtK.filter_sets.append(test_set)
    print('__compute_scores {}'.format(len(test_set.triples)))
    self.__compute_scores(result_set, test_set, hitsAtK)
    print('hits@1   hits@3    hits@10')
    h1 = hitsAtK.hits_adn_head_filtered[0] + hitsAtK.hits_adn_tail_filtered[0] / hitsAtK.counter_head + hitsAtK.counter_tail
    h3 = hitsAtK.hits_adn_head_filtered[2] + hitsAtK.hits_adn_tail_filtered[2] / hitsAtK.counter_head + hitsAtK.counter_tail
    h10 = hitsAtK.hits_adn_head_filtered[9] + hitsAtK.hits_adn_tail_filtered[9] / hitsAtK.counter_head + hitsAtK.counter_tail
    print('{}\t{}\t{}'.format(h1, h3, h10))
  
  def __compute_scores(self, result_set, gold, hitsAtK):
    for triple in gold.triples:
      cand1 = result_set.get_head_candidates(triple)
      hitsAtK.evaluate_head(cand1, triple)
      cand2 = result_set.get_tail_candidates(triple)
      hitsAtK.evaluate_tail(cand2, triple)