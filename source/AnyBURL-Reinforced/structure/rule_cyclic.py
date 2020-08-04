
from structure.rule import Rule
from structure.rule_untyped import RuleUntyped

class RuleCyclic(Rule):

  def __init__(self, rule_untyped):
    super().__init__()
    super().init_from_rule_untyped(rule_untyped)
    if self.body.literals[0].contains('Y') and self.bodysize() > 1:
      for i in range((self.bodysize() // 2) - 1 ):
        j = (self.bodysize() - i) - 1
        atom_i = self.body.literals[i]
        atom_j = self.body.literals[j]
        self.body.literals[i] = atom_j
        self.body.literals[j] = atom_i

      self.body.normalize_variable_names()

  def compute_tail_results(self):
    results = {}