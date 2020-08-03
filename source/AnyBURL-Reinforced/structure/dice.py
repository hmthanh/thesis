import sys
from random import random, randrange
from threading import RLock

from settings import Settings
from utilities import current_milli_time

class Dice(object):
  supported_types = 12
  supported_types_cyclic = 10
  gama = 0.0001
  initial_score = sys.float_info.max / (supported_types + 1)

  def __init__(self, output_path):
    self.output_path = output_path
    self.timestamps = []
    self.scores = []
    self.freqs = []
    self.current_scores = []
    self.current_freqs = []
    self.relevant_scores = []
    self.relevant_scores_computed = []
    self.resource_lock = RLock()
    self.cfg = Settings()
    self.cfg.load_learning_config()
    # init components
    for i in range(Dice.supported_types):
      self.current_scores.append(Dice.initial_score)
      self.current_freqs.append(1)
      self.relevant_scores.append(0)

    if self.cfg.max_length_acyclic == 0:
      self.current_scores[self.supported_types_cyclic] = 0.0
      self.current_scores[self.supported_types_cyclic + 1] = 0.0

    if self.cfg.max_length_acyclic == 1:
      self.current_scores[self.supported_types_cyclic + 1] = 0.0

    for j in range(self.cfg.max_length_cyclic, self.supported_types_cyclic):
      self.current_scores[j] = 0.0


  def ask(self, bath_counter):
    '''
    Throws a dice for the rule types which is weighted according to the scores collected the last time this type was mined.
    '''
    r = (self.cfg.randomized_decisions_annealing - bath_counter) / self.cfg.randomized_decisions_annealing
    if r < self.cfg.epsilon:
      r = self.cfg.epsilon
    if random() < r:
      i = randrange(Dice.supported_types )
      while self.scores[0][i] == 0:
        i = randrange(Dice.supported_types)
      return i

    if self.cfg.policy == 1:
      score = max(self.relevant_scores)
      self.relevant_scores.index(score)
    elif self.cfg.policy == 2:
      if not self.relevant_scores_computed:
        raise Exception('before asking the dice you have to compute the relevant scores')
      total = sum(self.relevant_scores)
      d = random() * total
      for i in range(self.supported_types):
        if d < self.relevant_scores[i]:
          return i
        d -= self.relevant_scores[i]

    return 0

  def compute_relevenat_scores(self):
    for i in range(self.supported_types):
      if self.current_scores[i] > 0:
        self.relevant_scores[i] = self.current_scores[i] / self.current_freqs[i]
    self.relevant_scores_computed = True

  def reset_scores(self):
    for i in range(self.supported_types):
      if self.current_scores[i] > 0:
        self.current_scores[i] = 0.0
        self.current_freqs[i] = 0
    self.relevant_scores_computed = False

  def add_score(self, index, score):
    if self.resource_lock.acquire():
      try:
        self.current_scores[index] += score
        self.current_freqs[index] += 1
        if score == 0:
          self.current_scores[index] += self.gama
      finally:
        self.resource_lock.release()

  def save_scores(self):
    self.scores.append([0 for i in range(self.supported_types)])
    self.freqs.append([0 for i in range(self.supported_types)])
    self.timestamps.append(current_milli_time())
    last_scores = self.scores[-1]
    last_freqs = self.freqs[-1]
    for i in range(len(self.current_scores)):
      last_freqs[i] = self.current_freqs[i]
      last_scores[i] = self.current_scores[i] / max(last_freqs[i], 1)

  def __str__(self):
    res = ''
    for i in range(self.supported_types):
      if i >= self.cfg.max_length_cyclic and i < self.supported_types_cyclic:
        continue
      if i - self.supported_types_cyclic >= self.cfg.max_length_acyclic:
        continue
      if i == self.supported_types_cyclic:
        res += ' |'
      s = self.relevant_scores[i]
      res += ' {}'.format(' > 99k' if s > 999999 else '{}'.format(int(s)))
    return res
  #####################################
  #####   static method   ############
  def simulate_score(type_score):
    if type_score == 3:
      return 100 + random() * 10
    if type_score == 5:
      return 100 + random() * 10
    return 10 + random() * 10

  def decoded_dice_cyclic(dice):
    return True if dice >= 0 and dice < Dice.supported_types_cyclic else False

  def decoded_dice_length(dice):
    return dice + 1 if Dice.decoded_dice_cyclic(dice) else dice - (Dice.supported_types_cyclic - 1)

  def encode(cyclic, length):
    return length - 1 if cyclic else (Dice.supported_types_cyclic - 1) + length