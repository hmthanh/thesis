from threading import Thread
from time import sleep

from structure.path import Path
from algorithm.path_sampler import PathSampler
from data.triple_set import TripleSet
from settings import Settings
from learn_reinforced import LearnReinforced


class ScorerReinforced(Thread):
  def __init__(self, triples, thread_id=1):
    threading.Thread.__init__(self)
    self.thread_id = thread_id
    self.triples = triples
    self.sampler = PathSampler(triples)
    self.mine_param_cyclic = True
    self.mine_param_length = 1
    self.ready = True
    self.only_XY = False

  def set_search_parameters(self, cyclic, length):
    self.mine_param_cyclic = cyclic
    self.mine_param_length = length
    self.ready = True
    self.only_XY = False
    if self.mine_param_cyclic:
      if self.mine_param_length > Settings.load_learning_config()['MAX_LENGTH_GROUNDED_CYCLIC']:
        self.only_XY = True


  def run(self):
    while not LearnReinforced.are_all_available():
      LearnReinforced.push_thread(self.id)
      sleep(20 / 1000)
    print('THREAD-{} starts to work with L = {} C = {} '.format(self.thread_id, self.mine_param_length, self.mine_param_cyclic))
    done = False
    while not done:

    print(str(self.thread_name) +"  "+ str(self.thread_id))