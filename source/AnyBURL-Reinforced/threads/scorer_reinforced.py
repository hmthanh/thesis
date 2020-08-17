from threading import Thread
from time import sleep

from structure.path import Path
from structure.rule_factory import RuleFactory
from algorithm.path_sampler import PathSampler
from data.triple_set import TripleSet
from settings import Settings
from learn_reinforced import LearnReinforced


class ScorerReinforced(Thread):

  def __init__(self, triples, thread_id=1):
    threading.Thread.__init__(self)
    self.thread_id = thread_id
    self.triples = triples
    self.sampler = PathSampler(triples)
    self.mine_param_cyclic = True
    self.mine_param_length = 1
    self.ready = True
    self.only_XY = False
    self.created_rules = 0
    self.stored_rules = 0
    self.produced_score = 0
    self.cfg = Settings()
    self.cfg.load_learning_config()

  def set_search_parameters(self, cyclic, length):
    self.mine_param_cyclic = cyclic
    self.mine_param_length = length
    self.ready = True
    self.only_XY = False
    if self.mine_param_cyclic:
      if self.mine_param_length > Settings.load_learning_config()['MAX_LENGTH_GROUNDED_CYCLIC']:
        self.only_XY = True


  def run(self):
    while not LearnReinforced.are_all_available():
      LearnReinforced.push_thread(self.id)
      sleep(20 / 1000)
    print('THREAD-{} starts to work with L = {} C = {} '.format(self.thread_id, self.mine_param_length, self.mine_param_cyclic))
    done = False
    while not done:
      if not LearnReinforced.is_active(self.thread_id, self.stored_rules, self.created_rules, self.produced_score, self.mine_param_cyclic, self.mine_param_length) or not self.ready:
        self.created_rules = 0
        self.stored_rules = 0
        self.produced_score = 0
        sleep(10 / 1000)
      else:
        ## search for cyclic rules
        if self.mine_param_cyclic:
          path = self.sampler.sample_path(self.mine_param_length + 1, True)
          if path is not None and path.is_valid():
            learned_rules = RuleFactory.getGeneralizations(path, self.only_XY)
            if not LearnReinforced.active:
              sleep(10 / 1000) # to do config
            else:
              for rule in learned_rules:
                self.created_rules += 1
                if rule.is_is_trivial():
                  continue
                if rule.is_redundant_AC_rule():
                  continue
                if LearnReinforced.is_stored(rule):
                  rule.compute_scores(self.triples)
                  if rule.confidence >= self.cfg.threshold_confidence and rule.correctly_predicted >= self.cfg.threshold_correct_prediction:
                    if LearnReinforced.active:
                      LearnReinforced.store_rule(rule)
                      self.produced_score += self.get_scoring_gain(rule, rule.correctly_predicted, rule.confidence, rule.get_applied_confidence())
                      self.stored_rules += 1

        if not self.mine_param_cyclic:
          path = self.sampler.sample_path(self.mine_param_length + 1, False)
          if path is not None and path.is_valid():
            learned_rules = RuleFactory.getGeneralizations(path, False)
            if not LearnReinforced.active:
              sleep(10 / 1000)
            else:
              for rule in learned_rules:
                self.created_rules += 1
                if rule.is_trivial():
                  continue
                if LearnReinforced.is_stored(rule):
                  try:
                    rule.compute_scores(self.triples)
                  except expression as identifier:
                    continue
                  if rule.confidence >= self.cfg.threshold_confidence and rule.correctly_predicted >= self.cfg.threshold_correct_prediction:
                    if LearnReinforced.active:
                      LearnReinforced.store_rule(rule)
                      self.produced_score += self.get_scoring_gain(rule, rule.correctly_predicted, rule.confidence, rule.get_applied_confidence())
                      self.stored_rules += 1


  def get_scoring_gain(self, rule, correctly_predicted, confidence, applied_confidence ):
    if self.cfg.reward == 1:
      return correctly_predicted
    elif self.cfg.reward == 2:
      return correctly_predicted * confidence
    elif self.cfg.reward == 3:
      return correctly_predicted * applied_confidence
    elif self.cfg.reward == 4:
      return correctly_predicted * applied_confidence**2
    elif self.cfg.reward == 5:
      return correctly_predicted * applied_confidence * (len(rule.bodysize() - 1) ** 2)

    return 0.0