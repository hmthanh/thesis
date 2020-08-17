from structure.atom import Atom

class Negation(object):

  def __init__(self, atom=Atom()):
    self.atom = atom

  def __hash__(self):
    return hash(self.atom) * -1

  def __eq__(self, that):
    if isinstance(that, self.__class__):
      return self.atom == that.atom
    return False

  def __str__(self):
    return '!{}'.format(str(self.atom))

  def get_right(self):
    return self.atom.right

  def get_left(self):
    return self.atom.left

  def get_relation(self):
    return self.atom.relation

  def is_variable_right(self):
    return len(self.atom.right) <= 1

  def is_variable_left(self):
    return len(self.atom.left) <= 1
