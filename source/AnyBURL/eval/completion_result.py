

class CompletionResult(object):

  def __init__(self, triple):
    self.triple = triple
    self.head_results = []
    self.tail_results = []
  
  def add_head_results(self, heads, k):
    if k > 0:
      self.add_results(heads, self.head_results, k)
    else:
      self.add_results(heads, self.headResults)

  def add_tail_results(self, tails, k):
    if k > 0:
      self.add_results(tails, self.tail_results, k)
    else:
      self.add_results(tails, self.tail_results)
  
  def add_results(self, candidates, results, k):
    for candidate in candidates:
      if candidate != '':
        results.append(candidate)
        k -= 1
        if k == 0:
          return

   def add_results(self, candidates, results):
    for candidate in candidates:
      if candidate != '':
        results.append(candidate)