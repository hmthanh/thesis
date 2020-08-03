import logging

from settings import Settings
from structure.dice import Dice

class LearnReinforced(object):
  available_threads = set()
  active = True
	report = False
	active_thread = []
  finished = False
  stats = []
  dice = None


  def __init__(self):
    logging.basicConfig(filename='learn.log',level=logging.DEBUG)
    logging.info('======================= start new section ======================')
    logging.info('Started LearnReinforced')
    self.cfg = Settings()
    self.cfg.load_learning_config()

    for i in range(cfg.worker_threads):
      stats.append([0, 0, 0])
      active_thread.append(False)


  def are_all_available():
    return True if len(available_threads) == cfg.learning_config['worker_threads'] else False

  def push_thread(id):
    available_threads.add(id)

  def is_active(thread_id, stored_rules, created_rules, produced_score, cyclic, length):
    if active:
      return True
    if not report:
      return True
    else if active_thread[thread_id]:
      type_str = Dice.encode(cyclic, length)
      stats[thread_id][0] = stored_rules
			stats[thread_id][1] = created_rules
      dice.add_score(type_str, producedScore)
      activeThread[thread_id] = False
      ### todo