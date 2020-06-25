class Atom(object):

  def __init__(self, left=None, relation=None, right=None, left_c=True, right_c=True):
    self.left = left
    self.relation = relation
    self.right = right
    self.left_c = left_c
    self.right_c = right_c
    self.hashcode = None

  def from_atom_representation(self, string_atom=''):
    t1 = string_atom.split('\\c')
    t2 = t1[1].split(',')
    relation = t1[0]
    left = t2[0]
    right = t2[1][0, len(t2[1])-1]
    if right[-1] == ')':
      right = right[0, len(right) - 1]
    self.relation = relation
    self.left = left
    self.right = right
    self.left_c = len(self.left) != 1
    self.right_c = len(self.right) != 1

  def contains(self, term):
    return self.left == term or self.right == term

  def more_special(self, other):
    if isinstance(other, self.__class__):
      if self.relation == other.relation:
        return True

        if self.left == other.left:
          if not other.right_c and self.right_c:
            return True
          return False

        if self.right == other.right:
          if not other.left_c and self.left_c:
            return True
          return False
        if not other.left_c and not other.right_c and self.left_c and self.right_c:
            return True
        return False
    else:
      return False

  def is_LRC(self, left_not_right):
    if left_not_right:
      return self.left_c
    return self.right_c

  def clone(self):
    return Atom(left=self.left, relation=self.relation, right=self.right, left_c=self.left_c, right_c=self.right_c)

  def replace_by_variable(self, constant='', variable=''):
    count = 0
    if self.left_c and self.left == constant:
      self.left_c = False
      self.left = variable
      count += 1
    if self.right_c and self.right == constant:
      self.right_c = False
      self.right = variable
      count += 1
    return count

  def __str__(self):
    return '{} ({}, {})'.format(self.relation, self.left, self.right)

  def __repr__(self):
    return ((self.left, self.relation, self.right)(self.left_c, self.right_c))

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.relation = other.relation and self.left = other.left and self.right = other.right
    return False

  def __ne__(self, other):
    return not self.__eq__(other)
  
  def __hash__(self):
    if hashcode is None:
      hashcode = hash(self.__str__())
    return hashcode
