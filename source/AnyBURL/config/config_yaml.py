import yaml

class Config(object):

  def __init__(self):
    pass
  
  def load_eval_config(self):
    with open('eval_config.yaml') as stream:
    # use safe_load instead load
      return yaml.safe_load(stream)