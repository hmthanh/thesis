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

    for line in lines:
      print(line)