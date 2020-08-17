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
    self.confidence = 0.0
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

  def check_negation(self, triple_set, variable, x_value):
    if self.negation is not None:
      if self.negation.get_left() == variable:
        tails = triple_set.get_tail_entities(self.negation.get_relation(), x_value)
        if self.negation.is_variable_right() and len(tails) > 0:
          return False
        elif self.negation.get_right() in tails:
          return False
      else:
        if self.negation.get_right() == variable:
          heads = triple_set.get_head_entities(self.negation.get_relation(), x_value)
        if self.negation.is_variable_left() and len(heads) > 0:
          return False
        elif self.negation.get_right() in heads:
          return False

    return True

  ########################################################
  #                 abstract method                     #
  #######################################################

  def compute_scores(self, triple_set):
    pass

  # Returns the tail results of applying this rule to a given head value.
  def compute_tail_results(self, head, triple_set):
    '''Returns the tail results of applying this rule to a given head value.'''
    pass

  def compute_head_results(self, head, triple_set):
    '''Returns the head results of applying this rule to a given tail value.'''
    pass

  def is_refinable(self):
    '''True, if this rule is refineable. False otherwise.'''
    pass

  def get_random_valid_prediction(self, triple_set):
    '''Returns a randomly chose triples that is both predicted and valid = true against the given triple set.'''
    pass

  def is_redundant_AC_rule(self, triples):
    '''
    Checks if a rule is a AC1 rule and if yes, if the last condition is for only a small number of entities true.
	  Such a rule can be (more or less) expressed by few  AC1 rule is one atom shorter.
    '''
    pass

  def materialize(self, training_set):
    pass

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
