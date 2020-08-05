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

  def load_learning_config(dataset='WN18'):
    with open('config/learning_config.yaml') as stream:
    # use safe_load instead load
      config_yaml = yaml.safe_load(stream)
      if dataset == 'WN18':
        config_yaml['path_training'] = config_yaml['path_training'][2]
      elif dataset == 'FB15k':
        config_yaml['path_training'] = config_yaml['path_training'][0]
      if dataset == 'FB15k-273':
        config_yaml['path_training'] = config_yaml['path_training'][1]
      if dataset == 'WN18RR':
        config_yaml['path_training'] = config_yaml['path_training'][3]
      config_yaml['dataset'] = dataset
      return config_yaml

  def load_predict_config():
    with open('config/predict_config.yaml') as stream:
    # use safe_load instead load
      return yaml.safe_load(stream)