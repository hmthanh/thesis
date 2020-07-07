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
  
''''TODO'''
  def _get_cyclic(self, current_variable, last_variable, value, body_index, direction, triples, previous_values, final_results, counter):
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
		head_not_tail = atom.left == currentVariable)
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
			Set<String> results = triples.getEntities(atom.getRelation(), value, headNotTail);
			// System.out.println("atom.getRelation()=" + atom.getRelation() + " value=" + value + " headNotTail=" + headNotTail);
			String nextVariable = headNotTail ? atom.getRight() : atom.getLeft();
			HashSet<String> currentValues = new HashSet<String>();
			currentValues.addAll(previousValues);
			currentValues.add(value);
			int i = 0;
			for (String nextValue : results) {
				if (!Rule.APPLICATION_MODE && i >= Learn.SAMPLE_SIZE) break;
				int updatedBodyIndex = (direction) ? bodyIndex + 1 : bodyIndex - 1;
				getCyclic(nextVariable, lastVariable, nextValue, updatedBodyIndex, direction, triples, currentValues, finalResults, count);
				i++;
			}
			return;
		}
	}
  
  def ground_body_cyclic(self, first_variable, last_variable, triples, sampling_on) {
		groundings = SampledPairedResultSet()
		atom = self.body.get(0);
		head_not_tail = atom.left == firstVariable
		rtriples = triples.get_triples_by_relation(atom.relation)
		counter = 0
		count = Counter()
		for triple in rtriples:
			counter += 1
			last_variable_groundings = set([])
			## Learn.takeTime();
		
			getCyclic(firstVariable, lastVariable, t.getValue(headNotTail), 0, true, triples, new HashSet<String>(), lastVariableGroundings, count);
			
			// Learn.showElapsedMoreThan(500, "call to getCyclic");
			
			if (lastVariableGroundings.size() > 0) {
				if (firstVariable.equals("X")) {
					groundings.addKey(t.getValue(headNotTail));
					for (String lastVariableValue : lastVariableGroundings) {
						groundings.addValue(lastVariableValue);
					}
				}
				else {
					for (String lastVariableValue : lastVariableGroundings) {
						groundings.addKey(lastVariableValue);
						groundings.addValue(t.getValue(headNotTail));
						
					}
				}
				
			}
			if ((counter >  Learn.SAMPLE_SIZE || groundings.size() > Learn.SAMPLE_SIZE) && samplingOn) {
				break;
			}
			if (!Rule.APPLICATION_MODE && count.get() >= Learn.TRIAL_SIZE) break;
		}
		return groundings;
	}

  def compute_scores(self, triples):
    if self.is_XY_rule():
			## X is given in first body atom
			xypairs = None
			if self.body.contains():
				xypairs = groundBodyCyclic("X", "Y", triples)
			else:
				xypairs = groundBodyCyclic("Y", "X", triples)
			// body groundings		
			int correctlyPredicted = 0;
			int predicted = 0;
			for (String key : xypairs.getValues().keySet()) {
				for (String value : xypairs.getValues().get(key)) {
					predicted++;
					if (triples.isTrue(key, this.head.getRelation(), value)) correctlyPredicted++;
				}
			}
			this.predicted = predicted;
			this.correctlyPredicted = correctlyPredicted;
			this.confidence = (double)correctlyPredicted / (double)predicted;
		}
		if (this.isXRule()) {
			HashSet<String> xvalues = new HashSet<String>();
			computeValuesReversed("X", xvalues, triples);
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