import logging

from settings import Settings
from structure.dice import Dice
from threading import RLock

class LearnReinforced(object):
  available_threads = set()
  active = True
	report = False
	active_thread = []
  finished = False
  stats = []
  dice = None
  # Lets hope that people will not run AnyBURl with more than 100 cores ... up to these 307 buckets should be sufficient
	# I somehow like the number 307
  rules307 = {}
  resource_lock = RLock()


  def __init__(self):
    logging.basicConfig(filename='learn.log',level=logging.DEBUG)
    logging.info('======================= start new section ======================')
    logging.info('Started LearnReinforced')
    self.cfg = Settings()
    self.cfg.load_learning_config()

    for i in range(cfg.worker_threads):
      stats.append([0, 0, 0])
      active_thread.append(False)

    for i in range(307):
      rules307[i] = set()


  def are_all_available():
    return True if len(available_threads) == cfg.learning_config['worker_threads'] else False

  def push_thread(id):
    available_threads.add(id)

  def is_active(thread_id, stored_rules, created_rules, produced_score, cyclic, length):
    if active:
      return True
    if not report:
      return True
    elif active_thread[thread_id]:
      type_str = Dice.encode(cyclic, length)
      stats[thread_id][0] = stored_rules
			stats[thread_id][1] = created_rules
      dice.add_score(type_str, produced_score)
      activeThread[thread_id] = False
      return False

    return False

  def is_stored(rule):
    code307 = abs(hash(rule)) % 307
    if code307 not in LearnReinforced.rules307[rule]:
      return True
    return False

  def store_rule(rule):
    '''
    Stores a given rule in a set. If the rule is a cyclic rule it also stores it in a way that is can be checked in
	  constants time for a AC1 rule if the AC1 follows.
    '''
    code307 = abs(hash(rule)) % 307
    if LearnReinforced.resource_lock.acquire():
      try:
        LearnReinforced.rules307[code307].add(rule)
        if isinstance(rule, RuleCyclic.__class__):
          index_XY_rule(rule)
      finally:
        LearnReinforced.resource_lock.release()

  def index_XY_rule(rule):
    print('implement index_XY_rule')
    pass