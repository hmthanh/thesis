from data.triple_set import TripleSet
from rule_io.rule_reader import RuleReader
from structure.rule_engine import RuleEngine
from apply_config import ApplyConfig
from structure.rule import Rule

class Apply(object):

  def __init__(self, path_rules, path_training, path_test, path_valid):
    '''/**
	 * Path to the rule file.
	 */'''
    self.path_rules = path_rules
    self.path_training = path_training
    self.path_test = path_test
    self.path_valid = path_valid
    self.path_rules_used = path_rules

  def prediction(self):
    Rule.application_mode = True
    training_set, test_set, valid_set = TripleSet(), TripleSet(), TripleSet()

    training_set.read_triples(self.path_training)
    test_set.read_triples(self.path_test)
    valid_set.read_triples(self.path_valid)

    rules = RuleReader(self.path_rules_used).read()
    rule_engine = RuleEngine()
    rule_engine.apply_rules_arx(rules, training_set, test_set, test_set, ApplyConfig.top_k_output)