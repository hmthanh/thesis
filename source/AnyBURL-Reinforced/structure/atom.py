from copy import deepcopy
class Atom(object):

  def __init__(self, left=None, relation=None, right=None, is_left_constant=True, is_right_constant=True):
    self.left = left
    self.relation = relation
    self.right = right
    self.is_left_constant = is_left_constant
    self.is_right_constant = is_right_constant
    self.hashcode = None

  def from_atom_representation(self, string_atom=''):
    t1 = string_atom.split('(')
    # print(t1)
    t2 = t1[1].split(',')
    relation = t1[0]
    left = t2[0]
    right = t2[1][0 : -1]
    if right[-1] == ')':
      right = right[0 : -1]
    self.relation = relation
    self.left = left.strip()
    self.right = right.strip()
    self.is_left_constant = len(self.left) != 1
    self.is_right_constant = len(self.right) != 1

  def get_XY_generalization(self):
    copy = self.clone()
    copy.left = 'X'
    copy.is_left_constant = False
    copy.right ='Y'
    copy.is_right_constant = False
    return copy

  def clone(self):
    return Atom(left=self.left, relation=self.relation, right=self.right, is_left_constant=self.is_left_constant, is_right_constant=self.is_right_constant)

  def equals(self, that, v_this, v_that):
    if self.relation != that.relation:
      return False
    if (self.left == v_this and that.left == v_that): #or (self.left == v_this and that.left == v_that)
      return True
    return False

  def to_string(self, indent):
    l = self.left
    r = self.right
    if indent > 0:
      if not self.is_left_constant and self.left != 'X' and self.left != 'Y':
        li = Rule.variables_to_indices.get(self.left)
        l = Rule.variables[li + indent]
      if not self.is_right_constant and self.right  != 'X' and self.right != 'Y':
        ri = Rule.variables_to_indices.get(this.right)
        r = Rule.variables[ri + indent]
    return '{}({},{})'.format(self.relation, l, r)

  def moreSpecial(self, atom):
    '''
    Returns true if this is more special than the given atom g.
    '''
    if self.relation == atom.relation:
      if self == atom:
        return True
      if self.left == atom.left:
        return True if not atom.is_right_constant and self.is_right_constant else False
    return False


  def moreSpecial_substituted(self, atom,  v_this, v_that):
    '''
    Returns true if this is more special than the given atom g, given that vThis is substituted by vThat.
    '''
    if self.relation == atom.relation:
      if self.left == v_this and atom.left == v_that:
        if not atom.is_right_constant and self.is_left_constant:
          return True
        return True if self.right == atom.right else False
      if self.right == v_this and atom.right == v_that:
        if not atom.is_left_constant and self.is_left_constant:
          return True
        return True if self.left == atom.left else False
    return False

  def replace_by_variable(self, constant, variable):
    i = 0
    if self.is_left_constant and self.left == constant:
      self.is_left_constant = False
      self.left = variable
      i += 1
    if self.is_right_constant and self.right == constant:
      self.is_right_constant = False
      self.right = variable
      i += 1
    return i

  def replace(self, val_old, val_new, block):
    if self.left == val_old and block != -1:
      self.left == val_new
      return -1
    if self.right == val_old and block != -1:
      self.right == val_new
      return 1
    return 0

  # shortcut getter left right constant
  def isLRC(self, left_not_right):
    return self.is_left_constant if left_not_right else self.is_right_constant

  # shortcut getter left right
  def getLR(self, left_not_right):
    return self.left if left_not_right else self.right

  def contains(self, term):
    return True if self.left == term or self.right == term else False

  def get_constant(self):
    if self.is_left_constant:
      return self.left
    return self.right if self.is_right_constant else None

  def is_inverse(self, pos):
    def compare_to(string, anotherString):
      len1, len2 = len(string), len(anotherString)
      lim = min(len1, len2)
      for i in range(lim):
        if string[i] != anotherString[i]:
          return string[i] - anotherString[i]
      return len1 - len2
    inverse = False
    if self.is_right_constant or self.is_left_constant:
      inverse = False if self.is_right_constant else True
    else:
      inverse = True if compare_to(self.right, self.left) < 0 else False
      if pos == 0:
        inverse = not inverse

    return inverse

  def get_variables(self):
    variables = set()
    if not self.is_left_constant and self.left != 'X' and self.left != 'Y':
      variables.add(self.left)
    if not self.is_right_constant and self.right != 'X' and self.right != 'Y':
       variables.add(self.right)
    return variables

  def get_other_term(self, term):
    if self.left == term:
      return self.right
    return self.left if self.right == term else None

  def to_string_const_val(self, const, val):
    return '{}({},{})'.format(self.relation, v if self.left == const else self.left, v if self.right == const else self.right)

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.relation == other.relation and self.left == other.left and self.right == other.right
    return False

  def __hash__(self):
    if self.hashcode is None:
      self.hashcode = hash(self.__str__())
    return self.hashcode

  def __str__(self):
    return '{}({},{})'.format(self.relation, self.left, self.right)