# this is abstract class
class Rule(object):
  variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
  application_mode = False
  variables_to_indices = {}

  def __init__(self, head=None):
    for i in range(len(Rule.variables)):
      Rule.variables[Rule.variables[i]] = i
    self.head = head
