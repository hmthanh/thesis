from data.triple import Triple
from settings import Settings
from random import choice
from asyncio import Lock

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
    self.confidence = None

    self.__read_triples(filepath)
    self.__index_triples()
    self.__setup_list_structure()

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

  def __setup_list_structure(self):
    print('* set up list structure ...')
    for head, rela in self.head_relation_to_tail.items():
      self.head_relation_to_tail_list[head] = {}
      for relation, val in rela.items():
        self.head_relation_to_tail_list.get(head)[relation] = []
        self.head_relation_to_tail_list.get(head)[relation].extend(val)

    for tail, rela in self.tail_relation_to_head.items():
      self.head_relation_to_tail_list[tail] = {}
      for relation, val in rela.items():
        self.tail_relation_to_head_list.get(tail)[relation] = []
        self.tail_relation_to_head_list.get(tail)[relation].extend(val)
    print(' done set up list structure')

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

  def get_triples_by_head(self, head):
    if head in self.head_to_list:
      return self.head_to_list.get(head)
    return []

  def get_triples_by_tail(self, tail):
    if tail in self.tail_to_list:
      return self.tail_to_list.get(tail)
    return []

  def get_triples_by_relation(self, relation):
    if relation in self.relation_to_list:
      return self.relation_to_list.get(relation)
    return []

  def get_random_triple_by_relation(self, relation):
    if relation in self.relation_to_list:
      return choice(self.relation_to_list.get(relation))
    return []

  def __compute_n_random_entities_by_relation(self, relation, head_not_tail, n):
    if relation in self.relation_to_list:
      entities = []
      for triple in self.relation_to_list.get(relation):
        val = triple.get_value(head_not_tail)
        if val not in entities:
          entities.append(val)
      sampled_entities = []
      for i in range(n):
        sampled_entities.append(choice(entities))
      if head_not_tail:
        self.relation_to_head_sample[relation] = sampled_entities
      else:
        self.relation_to_tail_sample[relation] = sampled_entities
      return sampled_entities
    else:
      print('something is strange, internal reference to relation  {}, which is not indexed'.format(relation))
      print('check if rule set and triple set fit together')
      return None

  def get_n_random_entities_by_relation(self, relation, head_not_tail, n):
    lock = Lock()
    async with lock:
      if head_not_tail:
        if relation in self.relation_to_head_sample:
          return self.relation_to_head_sample.get(relation)
      else:
        if relation in self.relation_to_tail_sample:
          return self.relation_to_tail_sample.get(relation)
      return self.__compute_n_random_entities_by_relation(relation, head_not_tail, n)

  def get_head_entities(self, relation, tail):
    if tail in self.tail_relation_to_head:
      if relation in self.tail_relation_to_head.get(tail):
        return self.tail_relation_to_head.get(tail).get(relation)
    else:
      return []

  def get_tail_entities(self, relation, head):
    if head in self.head_relation_to_tail:
      if relation in self.head_relation_to_tail.get(head):
        return self.head_relation_to_tail.get(head).get(relation)
    else:
      return []

  def get_entities(self, relation, value, head_not_tail):
    '''
    Returns those values for which the relation holds for a given value. If the head_not_tail is
	  set to true, the value is interpreted as head value and the corresponding tails are returned.
	  Otherwise, the corresponding heads are returned.
    '''
    if head_not_tail:
      return self.get_tail_entities(relation, value)
    else:
      return self.get_head_entities(relation, value)

  def get_random_tail_entity(self, relation, head):
    if head not in self.head_relation_to_tail_list:
      return None
    if relation not in self.head_relation_to_tail_list.get(head):
      return None
    return choice(self.head_relation_to_tail_list.get(head).get(relation))

  def get_random_head_entity(self, relation, tail):
    if tail not in self.tail_relation_to_head_list:
      return None
    if relation not in self.tail_relation_to_head_list.get(tail):
      return None
    return choice(self.tail_relation_to_head_list.get(tail).get(relation))

  def get_random_entity(self, relation, value, head_not_tail):
    '''
    Returns a random value for which the relation holds for a given value. If the head_not_tail is
	  set to true, the value is interpreted as head value and the corresponding tails are returned.
	  Otherwise, the corresponding heads are returned.
    '''
    if head_not_tail:
      return self.get_random_tail_entity(relation, value)
    return self.get_random_head_entity(relation, value)

  def get_relations(self, head, tail):
    tail_to_relation = self.head_tail_to_relation.get(head)
    if tail_to_relation is not None:
      relation = tail_to_relation.get(tail)
    return relation if relation is not None else set()

  def is_true(self, head, relation, tail):
    relation_to_head = self.tail_relation_to_head.get(tail)
    if relation_to_head is not None:
      if head in relation_to_head.get(relation):
        return True
    return False

  def is_true_triple(self, triple):
    return self.is_true(triple.head, triple.relation, triple.tail)

  def get_confidence(self, triple):
    if self.is_true(triple):
      return 1.0
    else:
      if triple in self.atriples:
        return self.atriples.get(triple)
      return 0.0

  def add_triple(self, triple):
    if self.is_true(triple) and triple not in self.atriples:
      return
    else:
      if triple.confidence == None:
        self.triples.append(triple)
        if triple in self.atriples:
          self.atriples.pop(triple)
        else:
          self.__add_triple_to_index(triple)
      else:
        new_confidence = triple.confidence
        if triple in self.atriples:
          stored_confidence = self.atriples.get(triple)
          if new_confidence > stored_confidence:
            self.atriples[triple] = new_confidence
        else:
          self.atriples[triple] = new_confidence
          self.__add_triple_to_index()

  def get_intersection_with(self, that):
    triple_set = TripleSet()
    for triple in self.triples:
      if that.is_true_triple(triple):
        triple_set.add_triple(triple)

    return triple_set

  def write(self, file_path):
    with output as open('file_path', 'w+'):
      for triple in self.triples:
        print(triple, file=output)
      for triple in self.atriples:
        print(triple, file=output)

  def size(self):
    return len(self.triples) + len(self.atriples)