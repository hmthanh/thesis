from atom import Atom

class Rule(object):
  variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
  def __init__(self, head):
    self.head = head
    self.body = []
    self.predicted = 0
	  self.correctly_predicted = 0
	  self.confidence = 0.0
	  self.next_free_variable = 0
	
  
  def init_from_path(self, path):
    self.body = []
		if path.markers[0] == '+' :
			self.head = Atom(path.nodes[0], path.nodes[1], path.nodes[2], True, True)
		else:
			self.head = new Atom(path.nodes[2], path.nodes[1], path.nodes[0], True, True)
	
		for i in range(len(path.markers)):
			if path.markers[i] == '+':
				#print("markers size = " + p.markers.length + "   nodes size = " + p.nodes.length + "   i =" +  i)
				self.body.add(new Atom(path.nodes[i*2], path.nodes[i*2+1], path.nodes[i*2+2], True, True))
			else:
				self.body.add(new Atom(p.nodes[i*2+2], p.nodes[i*2+1], p.nodes[i*2], True, True))
  
  def __replace_by_variable(self, constant, variable):
		count = self.head.replace_by_variable(constant, variable)
		for batom in self.body:
			bcount = batom.replace_by_variable(constant, variable);
			count += bcount		
		return count
	

  def __get_left_right_generalization(self):
    left_right_general = self.createCopy();
		left_constant = left_right_general.head.left
		xcount = left_right_general.__replace_by_variable(left_constant, 'X')
		right_constant = lrG.head.right
		ycount = left_right_general.__replace_by_variable(right_constant, 'Y')
		if xcount < 2 or ycount < 2:
      left_right_general = None
		return left_right_general

  def __replace_all_constants_by_variables(self):
		for atom in self.body:
			if atom.left_c:
				c = atom.left
				self.__replace_by_variable(c, Rule.variables[self.nextFreeVariable])
				self.next_free_variable += 1
			if atom.right_c:
				c = atom.right
				self.__replace_by_variable(c, Rule.variables[self.nextFreeVariable])
				self.next_free_variable += 1

  def get_generalizations(self, only_XY):
    generalizations = set([])
    left_right = self.__get_left_right_generalization()
		if left_right is not None:
			left_right.__replace_all_constants_by_variables()
			generalizations.add(left_right)
    if only_XY:
      return generalizations