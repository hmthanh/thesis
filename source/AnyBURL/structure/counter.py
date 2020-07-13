class Counter(object):

  def __init__(self):
    self.counter = 0
  
  def incomming(self):
    self.counter += 1
  
  def get(self):
    return self.counter

  def incomming_and_get(self):
    self.counter += 1
    return self.counter