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
