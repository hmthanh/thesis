from config.config_yaml import Config
from data.triple_set import TripleSet
from eval.result_set import ResultSet
from eval.hits_atk import HitsAtK
from structure.rule import Rule

class Evaluation(object):

  def __init__(self):
    Rule.set_application_mode()
    self.config = Config.load_eval_config()
    self.training_set, self.validation_set, self.test_set = TripleSet(), TripleSet(), TripleSet()
    self.training_set.read_triples(self.config['path_training'])
    self.validation_set.read_triples(self.config['path_valid'])
    self.test_set.read_triples(self.config['path_test'])
    self.result_set = ResultSet(self.config['path_prediction'], self.config['path_prediction'], True, 10)

  def eval(self):
    # print('result_set {}'.format(len(result_set.results)))
    hitsAtK = HitsAtK()
    hitsAtK.filter_sets.append(self.training_set)
    hitsAtK.filter_sets.append(self.validation_set)
    hitsAtK.filter_sets.append(self.test_set)
    self.__compute_scores(self.result_set, self.test_set, hitsAtK)
    print('hits@1   hits@3    hits@10')
    h1 = (hitsAtK.hits_adn_head_filtered[0] + hitsAtK.hits_adn_tail_filtered[0]) / (hitsAtK.counter_head + hitsAtK.counter_tail)
    h3 = (hitsAtK.hits_adn_head_filtered[2] + hitsAtK.hits_adn_tail_filtered[2]) / (hitsAtK.counter_head + hitsAtK.counter_tail)
    h10 = (hitsAtK.hits_adn_head_filtered[9] + hitsAtK.hits_adn_tail_filtered[9]) / (hitsAtK.counter_head + hitsAtK.counter_tail)
    print('{}\t{}\t{}'.format(h1, h3, h10))

  def __compute_scores(self, result_set, gold, hitsAtK):
    for triple in gold.triples:
      cand1 = result_set.get_head_candidates(str(triple))
      hitsAtK.evaluate_head(cand1, triple)
      cand2 = result_set.get_tail_candidates(str(triple))
      hitsAtK.evaluate_tail(cand2, triple)