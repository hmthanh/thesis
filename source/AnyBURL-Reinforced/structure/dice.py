import sys
from random import random, randint

from settings import Settings

class Dice(object):
  supported_types = 12
  supported_types_cyclic = 10
  gama = 0.0001
  cfg = Settings()
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
    # init components
    for i in range(Dice.supported_types):
      self.current_scores.append(Dice.initial_score)
      self.current_freqs.append(1)

    if cfg.max_length_acyclic == 0:
      self.current_scores[Dice.supported_types_cyclic] = 0.0f
      self.current_scores[Dice.supported_types_cyclic + 1] = 0.0f

    self.current_scores[Dice.supported_types_cyclic + 1] = 0.0 if cfg.max_length_acyclic == 1

    for j in range(cfg.max_length_acyclic, Dice.supported_types_cyclic):
      self.current_scores[j] = 0.0f


  def ask(self, bath_counter):
    '''
    Throws a dice for the rule types which is weighted according to the scores collected the last time this type was mined.
    '''
    r = (cfg.randomized_decisions_annealing - bath_counter) / cfg.randomized_decisions_annealing
    r = cfg.epsilon if r < cfg.epsilon
    if random() < r:
      i = 0
      while self.scores[0][i] == 0:
        i = randint(0, Dice.supported_types)
      return i
    if cfg.policy == 1:
      score = max(self.relevant_scores)
      self.relevant_scores.index(score)
    if cfg.policy == 2:
      raise Exception('before asking the dice you have to compute the relevant scores') if self.relevant_scores_computed
      total = sum(self.relevant_scores)
      d = random() * total
      for i in range(self.supported_types):
        return i if d < self.relevant_scores[i]
        d -= self.relevant_scores[i]

    return 0

  def compute_relevenat_scores(self):

    self.relevant_scores_computed = True
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