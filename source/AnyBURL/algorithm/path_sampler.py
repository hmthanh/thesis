from data.triple_set import TripleSet
from structure.path import Path

import random

class PathSampler(object):
  ''' This class is responsible for sampling grounded pathes.'''
  def __init__(self, triple_set):
    self.triple_set = triple_set
  
  def sample_path(self, steps, cyclic=False):
    triple = random.choice(self.triple_set.triples)
    nodes, markers = [None] * (1 + steps * 2), [None] * steps
    if triple.head == triple.tail:
      return None
    if random.uniform(0.0, 1.0) < 0.5:
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
      candidate_triples = None
      if random.uniform(0.0, 1.0) < 0.5:
        candidate_triples = self.triple_set.get_triples_by_head(nodes[index * 2])
        if candidate_triples is None or len(candidate_triples) == 0:
          return None
        next_triple = None
        if cyclic and index + 1 == steps:
          cyclic_candidate_triples = []
          for candidate in candidate_triples:
            if candidate.tail == nodes[0]:
              cyclic_candidate_triples.append(candidate)
          if len(cyclic_candidate_triples) == 0:
            return None
          next_triple = random.choice(cyclic_candidate_triples)
        else:
          next_triple = random.choice(candidate_triples)

        nodes[index * 2 + 1] = next_triple.relation
        nodes[index * 2 + 2] = next_triple.tail
        markers[index] = '+'
      else:
        candidate_triples = self.triple_set.get_triples_by_tail(nodes[index * 2])
        if candidate_triples is None or len(candidate_triples) == 0:
          return None
        next_triple = None
        if cyclic and index + 1 == steps:
          cyclic_candidate_triples = []
          for candidate in candidate_triples:
            if candidate.head == nodes[0]:
              cyclic_candidate_triples.append(candidate)
          if len(cyclic_candidate_triples) == 0:
            return None
          nextTriple = random.choice(cyclic_candidate_triples)
        else:
          nextTriple = random.choice(candidate_triples)

        nodes[index * 2 + 1] = nextTriple.relation
        nodes[index * 2 + 2] = nextTriple.head
        markers[index] = '-'

      index += 1

    return Path(nodes, markers)