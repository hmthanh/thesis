from data.triple import Triple
from settings import Settings

class TripleSet(object):
  cfg = Settings()
  def __init__(self, filepath='../../datasets/WN18/train.txt'):
    self.triples = []
    self.atriples = {}
    
    self.head_to_list = {}
    self.tail_to_list = {}
    self.relation_to_list = {}

    self.head_relation_to_tail = {}
    self.head_tail_to_relation = {}
    self.tail_relation_to_head = {}

    self.head_relation_to_tail_list = {}
    self.tail_relation_to_head_list = {}
    self.frequent_relations = set()

    self.relation_to_head_sample = {}
    self.relation_to_tail_sample = {}

    self.__read_triples(filepath)
    self.__index_triples()

  def __read_triples(self, filepath):
    with open(filepath, encoding='utf-8') as files:
      line_counter = 0
      for line in files:
        line = line.strip()
        line_counter += 1
        if line_counter % 1000000 == 0:
          print('>>> parsed {} lines'.format(line_counter))
        if len(line) <= 2:
          continue
        token = line.split('\t')
        triple = None
        if len(token) < 3:
          token = line.split(' ')
        elif len(token) == 3:
          triple = Triple(token[0], token[1], token[2])
        elif len(token) == 4:
          if token[3] == '.':
            triple = Triple(token[0], token[1], token[2])
          else:
            triple = Triple(token[0], token[1], token[2])
            triple.confidence = float(token[3])

        if triple != None:
          self.triples.append(triple)
          if self.cfg.rewrite_reflexiv and triple.tail == self.cfg.rewrite_reflexiv_token:
            trev = Triple(triple.tail, triple.relation, triple.head)
            trev.confidence = triple.confidence
            self.triples.append(trev)
    print('* read {} triples'.format(len(self.triples)))

  def __index_triples(self):
    counter, divisor = 0, 10000
    for triple in self.triples:
      counter += 1
      if counter % divisor == 0:
        print('* indexed {} triples'.format(counter))
        divisor *= 2
      self.__add_triple_to_index(triple)
    print('* set up index for {} relations, {} head entities, and {} tail entities'.format(len(self.relation_to_list), len(self.head_to_list), len(self.tail_to_list)))
  
  def __add_triple_to_index(self, triple):
    head, tail, relation = triple.head, triple.tail, triple.relation
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
      self.head_relation_to_tail[head] = dict()
    if relation not in self.head_relation_to_tail.get(head):
      self.head_relation_to_tail.get(head)[relation] = set()
    self.head_relation_to_tail.get(head).get(relation).add(tail)

    # index tail-relation => head
    if tail not in self.tail_relation_to_head:
      self.tail_relation_to_head[tail] = dict()
    if relation not in self.tail_relation_to_head.get(tail):
      self.tail_relation_to_head.get(tail)[relation] = set()
    self.tail_relation_to_head.get(tail).get(relation).add(head)

    # index headTail => relation
    if head not in self.head_tail_to_relation:
      self.head_tail_to_relation[head] = dict()
    if tail not in self.head_tail_to_relation.get(head):
      self.head_tail_to_relation.get(head)[tail] = set()
    self.head_tail_to_relation.get(head).get(tail).add(relation)