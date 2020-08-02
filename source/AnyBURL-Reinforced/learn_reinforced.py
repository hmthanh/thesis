import logging
from settings import Settings

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

  def are_all_available():
    return True if len(LearnReinforced.available_threads) == Settings.load_learning_config()['WORKER_THREADS'] else False

  def push_thread(id):
    LearnReinforced.available_threads.add(id)

  def is_active(thread_id, stored_rules, created_rules, produced_score, cyclic, length):
    if LearnReinforced.active:
      return True
    if not LearnReinforced.report:
      return True
    else if LearnReinforced.active_thread[thread_id]:
      type_str = Dice.encode(cyclic, length)
      stats[thread_id][0] = stored_rules
			stats[thread_id][1] = created_rules
      dice.add_score(type_str, producedScore)
      activeThread[thread_id] = False
      ### todo