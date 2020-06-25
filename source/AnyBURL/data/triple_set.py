from .triple import Triple

class TripleSet (object):

  def __init__(self):
    self.triples = []

    self.head_to_list = {}
    self.tail_to_list = {}
    self.relation_to_list = {}

    self.head_relation_to_tail = {}
    self.head_tail_to_relation = {}
    self.tail_relation_to_head = {}

    self.frequent_relations = set([])

  def read_triples(self, filepath):
    with open(filepath) as f:
      lines = f.readlines()
    lineCounter = 0
    for line in lines:
      lineCounter += 1
      if lineCounter % 1000000 == 0:
        print('>>> parsed {0} lines'.format(lineCounter))
      token = line.split('\t')

      if len(token) < 3:
        token = line.split(' ')

      if len(token) == 3:
        triple = Triple(token[0], token[1], token[2])
        self.triples.append(triple)

  def index_triples(self):
    counter = 0
    for triple in self.triples:
      counter += 1
      if counter % 100000 == 0:
        print('* indexed {} triples'.format(counter))
      self.__add_triple_to_index(triple)
    print('* set up index for {} relations, {} head entities, and {} tail entities'.format(len(self.relation_to_list.keys()), len(self.head_to_list.keys()), len(self.tail_to_list.keys())));

  def __add_triple_to_index(self, triple):
    head = triple.head
    tail = triple.tail
    relation = triple.relation

    # index head
    if head not in self.head_to_list:
      self.head_to_list[head] = []
    self.head_to_list.get(head).append(triple)

    # index tail
    if tail not in self.tail_to_list:
      self.tail_to_list[tail] = []
    self.tail_to_list.get(tail).append(triple)

    # index relation
    if relation not in self.relation_to_list:
      self.relation_to_list[relation] = []
    self.relation_to_list.get(relation).append(triple)

    # index head-relation => tail
    if head not in self.head_relation_to_tail:
      self.head_relation_to_tail[head] = {}
    if relation not in self.head_relation_to_tail.get(head):
      self.head_relation_to_tail.get(head)[relation] = set([])
    self.head_relation_to_tail.get(head).get(relation).add(tail)

    # index tail-relation => head
    if tail not in self.tail_relation_to_head:
      self.tail_relation_to_head[tail] = {}
    if relation not in self.tail_relation_to_head.get(tail):
      self.tail_relation_to_head.get(tail)[relation] = set([])
    self.tail_relation_to_head.get(tail).get(relation).add(head)

    # index head-tail => relation
    if head not in self.head_tail_to_relation:
      self.head_tail_to_relation[head] = {}
    if tail not in self.head_tail_to_relation.get(head):
      self.head_tail_to_relation.get(head)[tail] = set([])
    self.head_tail_to_relation.get(head).get(tail).add(relation)
