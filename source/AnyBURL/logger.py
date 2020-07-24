import logging
class Logger(object):
  logging.basicConfig(filename='log_debug/log.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                      datefmt='%H:%M:%S', level=logging.DEBUG)
  def __init__(self):
    pass

  def get_logger(class_name):
    return logging.getLogger(class_name)