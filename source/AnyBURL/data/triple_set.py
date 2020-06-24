from .triple import Triple

class TripleSet (object):

  def __init__(self):
    self.triples = []

    self.headToList = {}
    self.tailToList = {}
    self.relationToList = {}

    self.headRelation2Tail = {}
    self.headTail2Relation = {}
    self.tailRelation2Head = {}

    self.frequentRelations = set([])
    # self.readTriples(filepath)
		#self.indexTriples()

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