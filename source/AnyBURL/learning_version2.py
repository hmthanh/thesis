from algorithm.path_sampler import PathSampler
from structure.rule import Rule
from data.triple_set import TripleSet
from learn_config import ConfigParameters
from logger import Logger
from utilities import current_milli_time
import time
import _thread


class Learning(object):

  def __init__(self):
    self.log = Logger.get_logger('Learning')
    self.log.info('****************************start new section*************************************')
    self.log.info('initialize learning {}'.format(current_milli_time()))

