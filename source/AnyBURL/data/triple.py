class Triple(object):

  '''A triple represents a labeled edge a knowledge graph.'''
  def __init__(self, head, relation, tail):
    self.head = head
    self.relation = relation
    self.tail = tail

  def get_value(self, head_not_tail):
    if head_not_tail:
      return self.head;
    else:
      return this.tail

  def __str__(self):
    return '{0} {1} {2}'.format(self.head, self.relation, self.tail)

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.head == other.head and self.tail == other.tail and self.relation == other.relation
    return False

  def __ne__(self, other):
        return not self.__eq__(other)

  def __hash__(self):
    return hash(self.__str__())