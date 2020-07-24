import yaml

class Config(object):

  def __init__(self):
    pass

  def load_eval_config():
    with open('config/eval_config.yaml') as stream:
    # use safe_load instead load
      return yaml.safe_load(stream)

  def load_learning_config():
    with open('config/learning_config.yaml') as stream:
    # use safe_load instead load
      return yaml.safe_load(stream)