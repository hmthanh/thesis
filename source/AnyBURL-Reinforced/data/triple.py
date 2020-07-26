from settings import Settings

class Triple(object):

  '''A triple represents a labeled edge a knowledge graph.'''
  def __init__(self, head, relation, tail):
    if len(head) < 2 or len(tail) < 2:
      print('the triple set you are trying to load contains constants of length 1')
      print('a constant (entity) needs to be described by at least two letters')
      exit(1)
    self.head = head
    self.relation = relation
    cfg = Settings()
    if head == tail and cfg.rewrite_reflexiv:
      self.tail = cfg.rewrite_reflexiv_token
    else:
      self.tail = tail
    self.hash_code = None
    self.confidence = 0.0

  def get_value(self, head_not_tail):
    if head_not_tail:
      return self.head
    else:
      return self.tail

  def equals(self, head_not_tail, subject, rel, obj):
    if head_not_tail:
      return self.head == subject and self.tail == obj and self.relation == rel
    else:
      return self.head == obj and self.tail == subject and self.relation == rel

  def __str__(self):
    return '{} {} {} {}'.format(self.head, self.relation, self.tail, self.confidence)

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.head == other.head and self.tail == other.tail and self.relation == other.relation
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    if hash_code is None:
      hash_code = hash(self.head) + hash(self.tail) + hash(self.relation)
    return hash_code