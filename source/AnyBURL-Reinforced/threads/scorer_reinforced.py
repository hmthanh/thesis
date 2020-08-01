from threading import Thread

from structure.path import Path
from algorithm.path_sampler import PathSampler
from data.triple_set import TripleSet


class ScorerReinforced(Thread):
  def __init__(self, triples, thread_ID='thread_ID'):
    threading.Thread.__init__(self)
    self.thread_ID = thread_ID
    self.triples = triples
    self.sampler = PathSampler(triples)

  def run(self):
    print(str(self.thread_name) +"  "+ str(self.thread_ID));