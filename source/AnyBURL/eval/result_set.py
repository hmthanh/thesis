

class ResultSet(object):

  def __init__(self, name, file_path='', contains_confidences=False, k=10):
    self.results = {}
    self.name = name
    self.file_path = file_path
    self.contains_confidences = contains_confidences
    self.k = k