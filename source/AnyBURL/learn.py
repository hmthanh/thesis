from algorithm.path_sampler import PathSampler

class Learn(object):
'''/**
	* Number of maximal attempts to create body grounding. Every partial body grounding is counted.
	*/'''
	trial_size = 1000000

'''/**
	* Used for restricting the number of samples drawn for computing scores as confidence.
	*/'''
	sample_size = 1000

  def __init__(self, train_path='../../datasets/FB15k-237/test.txt'):
    self.triple_set = TripleSet()
    self.triple_set.read_triples(train_path)

  def train(self):
    print('* read {} triples'.format(len(self.triple_set.triples)))
    path_sampler = PathSampler(self.triple_set)
    all_useful_rules = []
    all_useful_rules.append({})
    while (True):
      pass