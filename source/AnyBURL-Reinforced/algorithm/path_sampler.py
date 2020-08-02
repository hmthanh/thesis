from structure.path import Path
from random import choice, random

class PathSampler(object):

  def __init__(self, triple_set):
    self.triple_set = triple_set
    pass

  def sample_path(self, steps, cyclic, chosen_head_triple=None, rule_to_be_extended=None):
    nodes, markers = [None] * (1 + steps * 2), [None] * steps
    chosen_triples = triple_set.triples
    triple = choice(chosen_triples) if chosen_head_triple == None else chosen_head_triple
    if triple.head == triple.tail:
      return None
    dice = random.random()
    if rule_to_be_extended is not None:
      if rule_to_be_extended.is_X_rule():
        dice = 1
      if rule_to_be_extended.is_Y_rule():
        dice = 0
    if dice < 0.5:
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
      if random() < 0.5:
        candidate_triples = self.triple_set.get_triples_by_head(nodes[index * 2])
        if len(candidate_triples) == 0:
          return None
        next_triple = None
        if cyclic and index + 1 == steps:
          cyclic_candidate_triples = []
          for candidate in candidate_triples:
            if candidate.tail == nodes[0]:
              cyclic_candidate_triples.append(candidate)
          if len(cyclic_candidate_triples) == 0:
            return None
          next_triple = choice(cyclic_candidate_triples)
        else:
          next_triple = choice(candidate_triples)

        nodes[index * 2 + 1] = next_triple.relation
        nodes[index * 2 + 2] = next_triple.tail
        markers[index] = '+'
      else:
        candidate_triples = self.triple_set.get_triples_by_tail(nodes[index * 2])
        if len(candidate_triples) == 0:
          return None
        next_triple = None
        if cyclic and index + 1 == steps:
          cyclic_candidate_triples = []
          for candidate in candidate_triples:
            if candidate.head == nodes[0]:
              cyclic_candidate_triples.append(candidate)
          if len(cyclic_candidate_triples) == 0:
            return None
          nextTriple = choice(cyclic_candidate_triples)
        else:
          nextTriple = choice(candidate_triples)

        nodes[index * 2 + 1] = nextTriple.relation
        nodes[index * 2 + 2] = nextTriple.head
        markers[index] = '-'

      index += 1
    p = Path(nodes, markers)
    return None if not cyclic and p.is_cyclic() else return p
