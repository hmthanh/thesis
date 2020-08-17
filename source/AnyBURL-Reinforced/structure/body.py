from structure.rule import Rule

class Body(object):

  def __init__(self):
    self.literals = []
    self.hashcode = None

  def add(self, atom):
    self.literals.append(atom)

  def size(self):
    return len(self.literals)

  def contains(self, atom):
    for item in self.literals:
      if item == atom:
        return True
    return False

  def get_last(self):
    '''
    Returns the last atom in this body.
    '''
    return self.literals[-1]

  def normalize_variable_names(self):
    old_to_new = {}
    index_new_variable_names = 0
    for atom in self.literals:
      variables = atom.get_variables()
      block = 0
      for value in variables:
        if value == 'X' or value == 'Y':
          continue
        if value not in old_to_new:
          v_new = Rule.variables[index_new_variable_names]
          old_to_new[value] = v_new
          index_new_variable_names += 1
        block = atom.replace_by_variable(value, old_to_new[value], block)

  def check_values_and_variables(self, variables_this_to_that, variables_that_to_this, atom1, atom2, left_not_right):
    if atom1.isLRC(left_not_right) and atom2.isLRC(left_not_right):
      if atom1.getLR(left_not_right) != atom2.getLR(left_not_right):
        return False
    #one variable and one constants do not fit
    if atom1.isLRC(left_not_right) != atom2.isLRC(left_not_right):
      return False
    if not atom1.isLRC(left_not_right) and not atom2.isLRC(left_not_right):
      # special cases X must be at same position as X, Y at same as Y
      if atom1.getLR(left_not_right) == 'X' and not atom2.getLR(left_not_right) == 'X':
        return False
      if atom2.getLR(left_not_right) == 'X' and not atom1.getLR(left_not_right) == 'X':
        return False
      if atom1.getLR(left_not_right) == 'Y' and not atom2.getLR(left_not_right) == 'Y':
        return False
      if atom2.getLR(left_not_right) == 'Y' and not atom1.getLR(left_not_right) == 'Y':
        return False
      that_v = variables_this_to_that.get(atom1.getLR(left_not_right))
      if that_v is not None:
        if atom2.getLR(left_not_right) != that_v:
          return False
      this_v = variables_that_to_this.get(atom2.getLR(left_not_right))
      if this_v is not None:
        if not atom1.getLR(left_not_right) == this_v:
          return False
      left_right1 = atom1.getLR(left_not_right)
      left_right2 = atom2.getLR(left_not_right)
      if left_right not in variables_this_to_that:
        variables_this_to_that[left_right1] = left_right2
        variables_this_to_that[left_right2] = left_right1

    return False

  def to_string(self, indent):
    return ', '.join([atom.to_string(indent) for atom in self.literals])

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      if len(other.literals) == len(self.literals):
        variables_this_to_that, variables_that_to_this = {}, {}
        for i in range(self.literals):
          atom1 = self.literals[i]
          atom2 = other.literals[i]
          if not atom1.relation == atom2.relation:
            return False
          else:
            if not check_values_and_variables(variables_this_to_that, variables_that_to_this, atom1, atom2, True):
              return False
            if not check_values_and_variables(variables_this_to_that, variables_that_to_this, atom1, atom2, False):
              return False
        return True
    return False

  def __hash__(self):
    if self.hashcode == None:
      body_string = ''.join([str(atom) for atom in self.literals])
      self.hashcode == hash(body_string)
    return self.hashcode

  def __str__(self):
    return ', '.join([str(atom) for atom in self.literals])