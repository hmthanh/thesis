from atom import Atom
from data.sampled_paired_result_set import SampledPairedResultSet
from counter import Counter
from apply import Apply
from learn import Learn

class Rule(object):
  variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
  application_mode = False
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
  
  def  is_XY_rule(self):
		if !self.head.is_left_constant and !self.head.is_right_constant:
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
		for body_literal : self.body:
			copy.body.add(body_literal.clone())
		copy.next_free_variable = self.next_free_variable;
		return copy

  def __get_left_right_generalization(self):
    left_right_general = self.__deep_copy()
		left_constant = left_right_general.head.left
		xcount = left_right_general.__replace_by_variable(left_constant, 'X')
		right_constant = lrG.head.right
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
			if atom.right_c:
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
			if atom.right_c:
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
		left = self.__get_left_generalization();
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
			if count >= Learn.trial_size or count >= Apply.trial_size:
        return
		if not Rule.application_mode and len(final_results) >= Learn.sample_size:
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
				## System.out.println("FINAL -> atom.getRelation()=" + atom.getRelation() + " value=" + value + " headNotTail=" + headNotTail);
			return
		## the current atom is not the last
		else: 
			results = triples.get_entities(atom.relation, value, head_not_tail)
			# System.out.println("atom.getRelation()=" + atom.getRelation() + " value=" + value + " headNotTail=" + headNotTail);
			next_variable = head_not_tail ? atom.right : atom.left
			current_values = previousValues.copy()
			current_values.add(value)
			for next_value in results:
				if not Rule.APPLICATION_MODE and i >= Learn.e):
          break
				updated_body_index = direction ? body_index + 1 : body_index - 1
				self._get_cyclic(next_variable, last_variable, next_value, updated_body_index, direction, triples, current_values, final_results, counter)
			return
	
  def ground_body_cyclic(self, first_variable, last_variable, triples, sampling_on):
		groundings = SampledPairedResultSet()
		atom = self.body.get(0);
		head_not_tail = atom.left == first_variable
		rtriples = triples.get_triples_by_relation(atom.relation)
		counter = 0
		count = Counter()
		for triple in rtriples:
			counter += 1
			last_variable_groundings = set([])
			## Learn.takeTime();
      triple_val = triple.get_value(head_not_tail)
			self._get_cyclic(first_variable, last_variable, triple_val, 0, true, triples, set([]), last_variable_groundings, count)
			
			# Learn.showElapsedMoreThan(500, "call to getCyclic");
			
			if len(last_variable_groundings) > 0:
				if firstVariable.equals('X'):
					groundings.add_key(triple_val)
					for last_variable_value in last_variable_groundings:
						groundings.add_value(last_variable_value) 
				else:
					for last_variable_value in last_variable_groundings:
						groundings.add_key(last_variable_value)
						groundings.add_key(triple_val)
			if (counter >  Learn.SAMPLE_SIZE or groundings.size() > Learn.SAMPLE_SIZE) and sampling_on:
				break
			if not Rule.APPLICATION_MODE and count.get() >= Learn.TRIAL_SIZE:
        break
		return groundings

  def get_unbound_variable(self):
		if self.body.get(len(self.body) - 1).is_left_constant or self.body.get(len(self.body) - 1-1).is_right_constant):
      return None
		counter = {}
		for atom : self.body:
			if not atom.left == 'X' and not atom.left == 'Y':
				if atom.left in counter:
          counter[atom.left] = 2
				else:
          counter[atom.left] = 1
			if not atom.right == 'X' and not atom..right == 'X':
				if atom.left in counter:
          counter[atom.right] = 2
				else:
          counter[atom.right] = 1
		for variable : counter.keys():
			if counter.get(variable) == 1:
				return variable
		return None

  def compute_values_reversed(self, target_variable, target_values, triple_set):
		atom_index = self.body.size() - 1
		last_atom = self.body.get(atom_index)
		unbound_variable = self.get_unbound_variable()
		if unbound_variable is None:
			next_var_is_left = False
			if last_atom.is_right_constant:
        next_var_is_left = True
			constant = last_atom.get_LR(not next_var_is_left)
			next_variable = last_atom.get_LR(next_var_is_left);
			values = triple_set.get_entities(last_atom.relation, constant, not next_var_is_left)
			previous_values = set([])
			previous_values.add(constant)
			for value in values:
        '''
        todo forwardReversed
        '''
				forwardReversed(nextVariable, value, atomIndex-1, targetVariable, targetValues, ts, previousValues);
				if !Rule.APPLICATION_MODE and targetValues.size() >= Learn.SAMPLE_SIZE:
          return
				
				if Rule.APPLICATION_MODE && targetValues.size() >= Apply.DISCRIMINATION_BOUND:
					targetValues.clear()
					return
		else :##
      '''
        todo else
        '''
			boolean nextVarIsLeft;
			if (lastAtom.getLeft().equals(unboundVariable)) nextVarIsLeft = false;
			else nextVarIsLeft = true;
			String nextVariable = lastAtom.getLR(nextVarIsLeft);
			ArrayList<Triple> triples = ts.getTriplesByRelation(lastAtom.getRelation());
			for (Triple t : triples) {
				String value = t.getValue(nextVarIsLeft);
				HashSet<String> previousValues = new HashSet<String>();
				String previousValue = t.getValue(!nextVarIsLeft);
				previousValues.add(previousValue);
				forwardReversed(nextVariable, value, atomIndex-1, targetVariable, targetValues, ts, previousValues);
				if (!Rule.APPLICATION_MODE && targetValues.size() >= Learn.SAMPLE_SIZE) return;
				
				if (Rule.APPLICATION_MODE && targetValues.size() >= Apply.DISCRIMINATION_BOUND) {
					targetValues.clear();
					return;
				}
				
			}
		}
	}

  def compute_scores(self, triples):
    if self.is_XY_rule():
			## X is given in first body atom
			xypairs = None
			# if self.body.contains():
			# 	xypairs = groundBodyCyclic("X", "Y", triples)
			# else:
			xypairs = ground_body_cyclic('Y', 'X', triples)
		  # body groundings		
			correctly_predicted = 0
			predicted = 0
			for key in xypairs.values.keys():
				for value : xypairs.values.get(key):
					predicted += 1
					if triples.isTrue(key, this.head.getRelation(), value):
            correctly_predicted += 1

			self.predicted = predicted
			self.correctly_predicted = correctly_predicted
			self.confidence = correctly_predicted / predicted
		if self.is_XY_rule():
			xvalues = set([])
			computeValuesReversed("X", xvalues, triples)
      ## TODO
			int predicted = 0, correctlyPredicted = 0;
			for (String xvalue : xvalues) {
				predicted++;
				if (triples.isTrue(xvalue, this.head.getRelation(), this.head.getRight())) correctlyPredicted++;
			}
			this.predicted = predicted;
			this.correctlyPredicted = correctlyPredicted;
			this.confidence = (double)correctlyPredicted / (double)predicted;
		}
		if (this.isYRule()) {
			HashSet<String> yvalues = new HashSet<String>();
			computeValuesReversed("Y", yvalues, triples);
			int predicted = 0, correctlyPredicted = 0;
			for (String yvalue : yvalues) {
				predicted++;
				if (triples.isTrue(this.head.getLeft(), this.head.getRelation(), yvalue)) correctlyPredicted++;
			}
			this.predicted = predicted;
			this.correctlyPredicted = correctlyPredicted;
			this.confidence = (double)correctlyPredicted / (double)predicted;
		}