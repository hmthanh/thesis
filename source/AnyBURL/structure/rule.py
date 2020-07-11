from structure.atom import Atom
from data.sampled_paired_result_set import SampledPairedResultSet
from structure.counter import Counter
from apply import Apply
from learn_config import ConfigParameters

class Rule(object):
  variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
  application_mode = False
  def __init__(self, head=None):
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
      self.head = Atom(path.nodes[2], path.nodes[1], path.nodes[0], True, True)
    
    for i in range(len(path.markers)):
      if path.markers[i] == '+':
        #print("markers size = " + p.markers.length + "   nodes size = " + p.nodes.length + "   i =" +  i)
        self.body.append(Atom(path.nodes[i*2], path.nodes[i*2+1], path.nodes[i*2+2], True, True))
      else:
        self.body.append(Atom(path.nodes[i*2+2], path.nodes[i*2+1], path.nodes[i*2], True, True))
  
  def  is_XY_rule(self):
    if not self.head.is_left_constant and not self.head.is_right_constant:
      return True
    else:
      return False

  def is_X_rule(self):
    if self.isXYRule():
      return False
    else:
      if not self.head.is_left_constant:
        return True
      else:
        return False
		
  def is_Y_rule(self):
    if self.isXYRule():
      return False
    else:
      if not this.head.is_right_constant:
        return True
      else:
        return False

  def __replace_by_variable(self, constant, variable):
    count = self.head.replace_by_variable(constant, variable)
    for batom in self.body:
      bcount = batom.replace_by_variable(constant, variable);
      count += bcount		
    return count
	
  def __deep_copy(self):
    copy = Rule(self.head.clone())
    for body_literal in self.body:
      copy.body.append(body_literal.clone())
    copy.next_free_variable = self.next_free_variable
    return copy

  def __get_left_right_generalization(self):
    left_right_general = self.__deep_copy()
    left_constant = left_right_general.head.left
    xcount = left_right_general.__replace_by_variable(left_constant, 'X')
    right_constant = left_right_general.head.right
    ycount = left_right_general.__replace_by_variable(right_constant, 'Y')
    if xcount < 2 or ycount < 2:
      left_right_general = None
    return left_right_general

  def __replace_all_constants_by_variables(self):
    for atom in self.body:
      if atom.is_left_constant:
        c = atom.left
        self.__replace_by_variable(c, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1
      if atom.is_right_constant:
        c = atom.right
        self.__replace_by_variable(c, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1

  def __get_left_generalization(self):
    left_generalization = self.__deep_copy()
    left_constant = left_generalization.head.left
    x_count = left_generalization.__replace_by_variable(left_constant, 'X')
    if x_count < 2: 
      left_generalization = None
    return left_generalization
	
  def __get_right_generalization(self):
    right_generalization = self.__deep_copy()
    right_constant = right_generalization.head.right
    y_count = right_generalization.__replace_by_variable(right_constant, 'Y')
    if y_count < 2:
      right_generalization = None
    return right_generalization

  def __replace_nearly_all_constants_by_variables(self):
    counter = 0
    for atom in self.body:
      counter += 1
      if counter == len(self.body):
        break
      if atom.is_left_constant:
        c = atom.left
        self.__replace_by_variable(c, Rule.variables[self.next_free_variable])
        self.next_free_variable += 1
      if atom.is_right_constant:
        c = atom.right
        self.__replace_by_variable(c, Rule.variables[self.next_free_variable]);
        self.next_free_variable += 1

  def get_generalizations(self, only_XY):
    generalizations = set([])
    left_right = self.__get_left_right_generalization()
    if left_right is not None:
      left_right.__replace_all_constants_by_variables()
      generalizations.add(left_right)
    
    if only_XY:
      return generalizations
    ## acyclic rule
    left = self.__get_left_generalization()
    if left is not None:
      left_free = left.__deep_copy()
      if left_right is None:
        left_free.__replace_all_constants_by_variables()
      left.__replace_nearly_all_constants_by_variables()
      generalizations.add(left)
      if left_right is None:
        generalizations.add(left_free)
    
    right = self.__get_right_generalization()
    if right is not None:
      right_free = right.__deep_copy()
      if left_right is None:
        right_free.__replace_all_constants_by_variables()
      right.__replace_nearly_all_constants_by_variables()
      generalizations.add(right)
      
      if left_right is None:
        generalizations.add(left_free)
    
    return generalizations

  def get_cyclic(self, current_variable, last_variable, value, body_index, direction, triples, previous_values, final_results, counter):
		# print("currentVariable=" + current_variable + " lastVariable=" +  last_variable + " value=" + value + " bodyIndex=" + body_index)
    if Rule.application_mode and len(final_results) >= Apply.discrimination_bound :
      final_results.clear()
    
    if counter is not None:
      count = counter.incomming_and_get()
      if count >= ConfigParameters.trial_size or count >= Apply.trial_size:
        return
    
    if not Rule.application_mode and len(final_results) >= ConfigParameters.sample_size:
      return
    # check if the value has been seen before as grounding of another variable
    atom = self.body.get(body_index)
    head_not_tail = atom.left == currentVariable
    if  value in previous_values:
      return		
    # the current atom is the last
    if (direction == True and len(self.body) -1 == body_index) or (direction == False and body_index == 0):
      # get groundings
      for v in triples.get_entities(atom.relation, value, head_not_tail):
        if v not in previous_values:
          final_results.add(v)
        print('FINAL -> atom.getRelation()=' + atom.relation + ' value=' + value + ' headNotTail=' + head_not_tail)
      return
    ## the current atom is not the last
    else: 
      results = triples.get_entities(atom.relation, value, head_not_tail)
      print("atom.getRelation()=" + atom.relation + " value=" + value + " headNotTail=" + head_not_tail);
      next_variable = atom.left
      if head_not_tail:
        next_variable = atom.right
      current_values = previous_values.copy()
      current_values.add(value)
      i = 0
      for next_value in results:
        if not Rule.application_mode and i >= ConfigParameters.sample_size:
          break
        updated_body_index =  body_index - 1
        if direction:
          updated_body_index = body_index + 1
        self._get_cyclic(next_variable, last_variable, next_value, updated_body_index, direction, triples, current_values, final_results, counter)
        i += 1
      return
	
  def ground_body_cyclic(self, first_variable, last_variable, triples, sampling_on=True):
    groundings = SampledPairedResultSet()
    atom = self.body[0]
    head_not_tail = atom.left == first_variable
    rtriples = triples.get_triples_by_relation(atom.relation)
    counter = 0
    count = Counter()
    for triple in rtriples:
      counter += 1
      last_variable_groundings = set([])
      ## Learn.takeTime()
      triple_val = triple.get_value(head_not_tail)
      self._get_cyclic(first_variable, last_variable, triple_val, 0, true, triples, set([]), last_variable_groundings, count)

      # Learn.showElapsedMoreThan(500, "call to getCyclic")
      
      if len(last_variable_groundings) > 0:
        if firstVariable.equals('X'):
          groundings.add_key(triple_val)
          for last_variable_value in last_variable_groundings:
            groundings.add_value(last_variable_value) 
        else:
          for last_variable_value in last_variable_groundings:
            groundings.add_key(last_variable_value)
            groundings.add_key(triple_val)
      if (counter >  ConfigParameters.sample_size or groundings.size() > ConfigParameters.sample_size) and sampling_on:
        break
      if not Rule.application_mode and count.get() >= ConfigParameters.trial_size:
        break
    return groundings

  def get_unbound_variable(self):
    if self.body.get(len(self.body) - 1).is_left_constant or self.body.get(len(self.body) - 1-1).is_right_constant:
      return None
    counter = {}
    for atom in self.body:
      if not atom.left == 'X' and not atom.left == 'Y':
        if atom.left in counter:
          counter[atom.left] = 2
        else:
          counter[atom.left] = 1
      
      if not atom.right == 'X' and not atom.right == 'X':
        if atom.left in counter:
          counter[atom.right] = 2
        else:
          counter[atom.right] = 1
          
    for key, value in counter:
      if value == 1:
        return key
    
    return None

  def forward_reversed(self, variable, value, body_index, target_variable, target_values={}, triple_set=set([]), previous_values={}):
    if value in previous_values:
      return
    if body_index < 0:
      target_values.add(value)
    else:
      current_values = set([])
      current_values.add(value)
      atom = self.body.get(body_index)
      next_var_is_left = False
      if atom.left != variable:
        next_var_is_left = True
      next_variable = atom.get_LR(next_var_is_left)
      next_values = set([])
      if not Rule.application_mode and len(target_variable) >= ConfigParameters.sample_size:
        return
      next_values = set(triple_set.get_entities(atom.relation, value, not next_var_is_left))
      for next_value in next_values:
        forwardReversed(next_variable, next_value, body_index - 1, target_variable, next_values, triple_set, current_values)

  def compute_values_reversed(self, target_variable, target_values, triple_set):
    atom_index = self.body.size() - 1
    last_atom = self.body.get(atom_index)
    unbound_variable = self.get_unbound_variable()
    if unbound_variable is None:
      next_var_is_left = False
      if last_atom.is_right_constant:
        next_var_is_left = True
      constant = last_atom.get_LR(not next_var_is_left)
      next_variable = last_atom.get_LR(next_var_is_left)
      values = triple_set.get_entities(last_atom.relation, constant, not next_var_is_left)
      previous_values = set([])
      previous_values.add(constant)
      
      for value in values:
        self.forward_reversed(next_variable, value, atom_index - 1, target_variable, target_values, triple_set, previous_values)
        if not Rule.application_mode and len(target_values) >= ConfigParameters.sample_size:
          return

        if Rule.application_mode and len(target_values) >= Apply.discrimination_bound:
          target_values.clear()
          return
    else :
      next_var_is_left = False
      if last_atom.left != unboundVariable:
        next_var_is_left = True
      next_variable = last_atom.get_LR(next_var_is_left)
      triples = triple_set.get_triples_by_relation(last_atom.relation)
      
      for triple in triples:
        value = triple.get_value(next_var_is_left)
        previous_values = set([])
        previous_value = triple.get_value(not next_var_is_left)
        previous_values.add(previous_value)
        self.forwardReversed(next_variable, value, atom_index - 1, target_variable, target_values, triple_set, previous_values)
        
        if not Rule.application_mode and len(target_values) >= ConfigParameters.sample_size:
          return
          
        if Rule.application_mode and len(target_values) >= Apply.discrimination_bound:
          target_values.clear()
          return

  def compute_scores(self, triples):
    if self.is_XY_rule():
			## X is given in first body atom
      xypairs = None
			# if self.body.contains():
			# 	xypairs = groundBodyCyclic("X", "Y", triples)
			# else:
  def compute_scores(self, triples):
    xypairs = self.ground_body_cyclic('Y', 'X', triples)
    # body groundings		
    correctly_predicted, predicted = 0, 0
    for key in xypairs.values.keys():
      for value in xypairs.values.get(key):
        predicted += 1
        if triples.is_true(key, self.head.relation, value):
          correctly_predicted += 1
      
      self.predicted = predicted
      self.correctly_predicted = correctly_predicted
      self.confidence = correctly_predicted / predicted
    
    if self.is_X_rule():
      xvalues = set([])
      self.compute_values_reversed('X', xvalues, triples)
      predicted, correctly_predicted = 0,0
      for xvalue in xvalues:
        predicted += 1
        if triples.is_true(xvalue, self.head.relation, self.head.right):
          correctly_predicted += 1
      self.predicted = predicted
      self.correctly_predicted = correctly_predicted
      self.confidence = predicted / correctly_predicted
    
    if self.is_Y_rule():
      yvalues = set([])
      self.compute_values_reversed('Y', yvalues, triples)
      predicted , correctly_predicted = 0,0
      for yvalue in yvalues:
        predicted += 1
        if triples.is_true(self.head.left, self.head.relation, yvalue):
          correctly_predicted += 1
          
      self.predicted = predicted
      self.correctly_predicted = correctly_predicted
      self.confidence = correctly_predicted / predicted

  def is_trivial(self):
    if len(self.body) == 1:
      if self.head == self.body[0]:
        return True
    return False
	