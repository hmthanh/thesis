
from structure.rule import Rule

class RuleUntyped(Rule):

  def __init__(self, head=None):
    super().__init__(head)

  def is_cyclic(self):
    if (self.head == None):
      return False
    return False if self.head.is_left_constant or self.head.is_right_constant else True

  def is_acyclic1(self):
    if self.is_cyclic():
      return False
    else:
      return True if self.body.literals[-1].is_left_constant or self.body.literals[-1].is_right_constant else False

  def is_acyclic2(self):
    if self.is_cyclic():
      return False
    else:
      return False if self.body.literals[-1].is_left_constant or self.body.literals[-1].is_right_constant else True

  def init_measure(self, predicted, correctly_predicted, confidence):
    self.predicted = predicted
    self.correctly_predicted = correctly_predicted
    self.confidence = confidence

  def get_left_right_generalization(self):
    left_right_generalization = self.clone()
    left_constant = left_right_generalization.head.left
    x_count = left_right_generalization.replace_by_variable(left_constant, 'X')
    right_constant = left_right_generalization.head.right
    y_count = lrG.replace_by_variable(right_constant, 'Y')
    if x_count < 2 or y_count < 2:
      left_right_generalization = None
    return left_right_generalization

  def get_left_generalization(self):
    left_rule_generalization = self.clone()
    left_constant = left_rule_generalization.head.left
    x_count = left_rule_generalization.replace_by_variable(left_constant, 'X')
    if x_count < 2:
      left_rule_generalization == None
    return left_rule_generalization

  def get_right_generalization(self):
    right_rule_generalization = self.clone()
    right_constant = right_rule_generalization.head.right
    x_count = right_rule_generalization.replace_by_variable(right_constant, 'Y')
    if x_count < 2:
      right_rule_generalization == None
    return right_rule_generalization

  def clone(self):
    copy = RuleUntyped(self.head.clone())
    for body_literal in self.body:
      copy.body.add(body_literal.clone())
    copy.next_free_variable = self.next_free_variable
    return copy

  def replace_by_variable(self, constant, variable):
    count = self.head.replace_by_variable(constant, variable)
    for atom in self.body.literals:
      b_count = atom.replace_by_variable(constant, variable)
      count += b_count
    return count

  def replace_nearly_all_constants_by_variables(self):
    counter = 0
    for atom in self.body.literals:
      counter += 1
      if counter == self.body.size():
        break
      if atom.is_left_constant:
        const = atom.left
        self.replace_by_variable(const, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1
      if atom.is_right_constant:
        const = atom.right
        self.replace_by_variable(const, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1

  def replace_all_constants_by_variables(self):
    for atom in self.body.literals:
      if atom.is_left_constant:
        const = atom.left
        self.replace_by_variable(const, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1
      if atom.is_right_constant:
        const = atom.right
        self.replace_by_variable(const, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1
