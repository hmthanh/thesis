from structure.body import Body
from settings import Settings

# this is abstract class
class Rule(object):
  variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
  application_mode = False
  variables_to_indices = {}

  def __init__(self, head=None):
    for i in range(len(Rule.variables)):
      Rule.variables[Rule.variables[i]] = i
    self.head = head
    self.body = Body()
    self.confidence = 0
    self.correctly_predicted = 0
    self.predicted = 0
    self.negation = None
    self.previous_confidence = 0
    self.next_free_variable = 0
    self.cfg = Settings()
    self.cfg.load_learning_config()
    self.hash_code = None

  def init_from_rule_untyped(self, rule_untyped):
    self.body = rule_untyped.body
    self.head = rule_untyped.head
    self.confidence = rule_untyped.confidence
    self.correctly_predicted = rule_untyped.correctlyPredicted
    self.predicted = rule_untyped.predicted
    self.negation = rule_untyped.negation

  def has_negation(self):
    return False if self.negation == None else True

  def set_application_mode():
    Rule.application_mode = True

  def add_body_atom(self, atom):
    self.body.add(atom)

  def get_body_atom(self, index):
    return self.body.literals[index]

  def get_target_relation(self):
    self.head.relation

  def bodysize(self):
    return len(self.body.literals)

  def is_trivial(self):
    if self.bodysize() == 1:
      if self.head == self.body.literals[0]:
        return True
    return False

  def get_applied_confidence(self):
    return self.correctly_predicted / (self.predicted + self.cfg.unseen_negative_examples)

  def is_XY_rule(self):
    return False if self.head.is_left_constant or self.head.is_right_constant else True

  def is_X_rule(self):
    if self.is_XY_rule():
      return False
    return True if not self.head.is_left_constant else False

  def is_Y_rule(self):
    if self.is_XY_rule():
      return False
    return True if not self.head.is_right_constant else False

  def __eq__(self, that):
    if isinstance(that, self.__class__):
      if self.head == that.head and self.body == that.body:
        if self.negation == None and that.negation == None:
          return True
        elif self.negation == that.negation:
          return True
        else:
          return False
    return False

  def __hash__(self):
    if self.hash_code == None:
      relation = ''.join([atom.relation for atom in self.body.literals])
      self.hash_code = hash(relation + str(self.negation))
    return self.hash_code

  def check_negation(self):
