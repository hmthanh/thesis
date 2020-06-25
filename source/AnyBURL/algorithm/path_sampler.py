from data.triple_set import TripleSet
from structure.path import Path

import random

class PathSampler():
  ''' This class is responsible for sampling grounded pathes.'''
  def __init__(self, triple_set):
    self.triple_set = triple_set
  
  def sample_path(self, steps, cyclic=False):
    triple = random.choice(triple_set)
    nodes,markers = [None] * steps, [None] * (1 + steps * 2)
    if triple.head == triple.tail:
      return None
    if random.random() < 0.5:
      markers[0] = '+'
      nodes[0] = triple.head
			nodes[1] = triple.relation
			nodes[2] = triple.tail
    else:
      markers[0] = '-'
			nodes[2] = triple.head
			nodes[1] = triple.relation
			nodes[0] = triple.tail
    # add next hop
    index = 1
    while index < steps:
      if random.random() < 0.5:
        candidateTriples = triple_set.get_triples_by_head(nodes[index * 2])
      next_triple = None
      if cyclic and index + 1 == steps: