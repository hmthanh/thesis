from algorithm.path_sampler import PathSampler
from structure.rule import Rule
from data.triple_set import TripleSet
from learn_config import ConfigParameters
from logger import Logger
from utilities import current_milli_time
from config.config_yaml import Config
import time
import _thread


class Learning(object):

  def __init__(self):
    self.log = Logger.get_log_cate('learning.txt', 'Learning')
    self.cfg = Config.load_learning_config()
    self.log.info('****************************start new section*************************************')
    self.log.info('initialize learning {}'.format(current_milli_time()))

  def train(self):
    index_start_time = current_milli_time()
    triple_set = TripleSet()
    triple_set.read_triples(self.cfg['path_training'])
    path_sampler = PathSampler(triple_set)
    path_counter, batch_counter = 0, 0
    batch_previously_found_rules, batch_new_useful_rules, batch_rules = 0, 0, 0
    mine_cyclic_not_acyclic = False
    all_useful_rules = [set()]
    snapshot_index, rule_size_cyclic, rule_size_acyclic = 0, 0, 0
    last_cyclic_coverage, last_acyclic_coverage = 0.0,0.0
    self.log.info('indexing dataset: {}'.format(self.cfg['path_training']))
    self.log.info('time elapsed: {} ms'.format(current_milli_time() - index_start_time))

    start_time = current_milli_time()
    while True:
      rule_size = rule_size_cyclic if mine_cyclic_not_acyclic else rule_size_acyclic
      useful_rules = all_useful_rules[rule_size]
      elapsed_seconds = (current_milli_time() - start_time) // 1000
      ## snapshots rule affter t seconds white learning
      snapshots_at = self.cfg['snapshots_at']
      if elapsed_seconds > snapshots_at[snapshot_index]:
        snapshot_index += 1
        print('CREATED SNAPSHOT {} after {} seconds'.format(snapshot_index, elapsed_seconds))
        if snapshot_index == len(snapshots_at):
          print('*************************done learning*********************************')
          return 0
      # batch learnig
      batch_start_time = current_milli_time()
      while True:
        if current_milli_time() - batch_start_time > self.cfg['batch_time']:
          break
        path_counter += 1
        path = path_sampler.sample_path(rule_size + 2, mine_cyclic_not_acyclic)
        if path != None and path.is_valid():
          rule = Rule()
          rule.init_from_path(path)
          gen_rules = rule.get_generalizations(mine_cyclic_not_acyclic)
          for r in gen_rules:
            if r.is_trivial():
              continue
            batch_rules += 1
            if r not in useful_rules:
              r.compute_scores(triple_set)
            if r.confidence >= self.cfg['threshold_confidence'] and r.correctly_predicted >= self.cfg['threshold_correct_predictions']:
              batch_new_useful_rules += 1
              useful_rules.add(r)
            else:
              batch_previously_found_rules += 1

      batch_counter += 1
      str_type = 'CYCLIC' if mine_cyclic_not_acyclic else 'ACYCLIC'
      print('>>> ****** Batch [{} {}] {} (sampled {} pathes) *****'.format(str_type, rule_size + 1, batch_counter, path_counter))
      current_coverage = batch_previously_found_rules / (batch_new_useful_rules + batch_previously_found_rules)
      print('>>> fraction of previously seen rules within useful rules in this batch: {} NEW = {} PREV = {} ALL = {}'.format(current_coverage,batch_new_useful_rules, batch_previously_found_rules, batch_rules))
      print('>>> stored rules: {}'.format(len(useful_rules)))
      if mine_cyclic_not_acyclic:
        last_cyclic_coverage = current_coverage
      else:
        last_cyclic_coverage = current_coverage

      if current_coverage > self.cfg['saturation'] and batch_previously_found_rules > 1:
        rule_size += 1
        if mine_cyclic_not_acyclic:
          rule_size_cyclic = rule_size
        if not mine_cyclic_not_acyclic:
          rule_size_acyclic = rule_size
        print('>>> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print('>>> INCREASING RULE SIZE OF {} RULE TO {}'.format(str_type, rule_size + 1))
        self.log.info('increasing rule size of {} rules to {}  after {} s'.format(str_type, rule_size + 1, (current_milli_time() - start_time)//1000))
        all_useful_rules.append(set())

      batch_new_useful_rules = 0
      batch_rules = 0
      batch_previously_found_rules = 0

      mine_cyclic_not_acyclic = not mine_cyclic_not_acyclic
      if mine_cyclic_not_acyclic and rule_size_cyclic + 1 > self.cfg['max_length_cylic']:
        mine_cyclic_not_acyclic = False
