# -*- coding: utf-8 -*-
# author: Phan Minh Tâm
# source has refer to java source of BURL method: http://web.informatik.uni-mannheim.de/AnyBURL/IJCAI/ijcai19.html file Config.java

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
  def load_predict_config():
    with open('config/predict_config.yaml') as stream:
    # use safe_load instead load
      return yaml.safe_load(stream)