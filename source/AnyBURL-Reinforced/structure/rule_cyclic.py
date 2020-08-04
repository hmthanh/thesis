
from structure.rule import Rule
from structure.rule_untyped import RuleUntyped


class RuleCyclic(Rule):

  def __init__(self, rule_untyped):
    super().__init__()
    super().init_from_rule_untyped(rule_untyped)
    if self.body.literals[0].contains('Y') and self.bodysize() > 1:
      for i in range((self.bodysize() // 2) - 1 ):
        j = (self.bodysize() - i) - 1
        atom_i = self.body.literals[i]
        atom_j = self.body.literals[j]
        self.body.literals[i] = atom_j
        self.body.literals[j] = atom_i

      self.body.normalize_variable_names()

  def compute_tail_results(self, head, triple_set):
    results = set()
    self.get_cyclic('X', 'Y', head, 0, True, triple_set, set(), results)
    return results

  def compute_head_results(self, tail, triple_set):
    results = set()
    self.get_cyclic('Y', 'X', tail, self.bodysize() - 1, False, triple_set, set(), results)
    return results

  def compute_scores(triple_set):
    pass

  def get_cyclic(self, current_variable, last_variable, value, body_index, direction, triple_set ,previous_values, final_results):
    if self.has_negation():
      if self.negation.left == current_variable:
        tails = triple_set.get_tail_entities(self.negation.relation, value)
        if self.negation.is_variable_right():
          if len(tails) > 0:
            return
      elif self.negation.right == current_variable:
        heads = triple_set.get_head_entities(self.negation.relation, value)
    if Rule.application_mode and len(final_results) >= self.cfg.discrimination_bound:
      final_results.clear()
      return
    # XXX if (!Rule.APPLICATION_MODE && finalResults.size() >= Settings.SAMPLE_SIZE) return;
		# check if the value has been seen before as grounding of another variable
    atom = self.body.literals[body_index]
    head_not_tail = atom.left == current_variable
    if value in previous_values:
      return
    if (direction == True and self.body.size() - 1 == body_index) and (direction == False and body_index == 0):
      for v in triple_set.get_entities(atom.relation, value, head_not_tail):
        if v not in previous_values and not v == value:
          final_results.add(v)
      return
    # the current atom is not the last
    else:
      results = triples.get_entities(atom.relation, value, head_not_tail)
      next_variable = atom.right if head_not_tail else atom.left
      current_values = set(previous_values)
      current_values.add(value)
      for next_value in results:
        updated_body_index = bodyIndex + 1 if direction else bodyIndex - 1
        self.get_cyclic(next_variable, last_variable, next_value, updated_body_index, direction, triple_set, current_values, final_results)
      return

