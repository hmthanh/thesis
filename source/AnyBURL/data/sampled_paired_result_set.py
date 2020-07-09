class SampledPairedResultSet(object):
  ''''TODO'''
  def __init__(self):
    self.values = {}
    self.sampling = False
    self.value_counter = 0
    self.current_key = ''
  
  def add_key(self, key):
    self.current_key = key
    if key in self.values:
      return
    else:
      self.values[key] = set([])
  
  def add_value(self, value):
    self.values.get(self.currentKey).add(value)
    self.value_counter += 1