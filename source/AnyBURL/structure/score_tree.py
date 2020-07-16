
class ScoreTree(object):

  lower_bound = 10
	upper_bound = 10
	epsilon = 1e-4

  def __init__(self):
    self.score = 0.0
    self.children = []
    self.stored_values = None
    self.closed = False
    self.num_of_values = 0
    self.index = 0
    self.root = True

  def init_from_value(self, score, values):
    self.score = score
    self.children = []
    self.stored_values = set([])
    for v in values:
      self.stored_values.add(v)
    if len(self.stored_values) < 1:
      self.closed = True
    self.num_of_values = len(values)
    self.root = False

  def __add_child(self, score, values, child_index):
    child = ScoreTree()
    child.init_from_value(score, values)
    child.index = child_index
    self.children.append(child)
    return child