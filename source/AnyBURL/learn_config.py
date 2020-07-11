class ConfigParameters(object):
  '''/**
	* Number of maximal attempts to create body grounding. Every partial body grounding is counted.
	*/'''
  trial_size = 1000000

  '''/**
	* Used for restricting the number of samples drawn for computing scores as confidence.
	*/'''
  sample_size = 1000
  '''/**
	 * The time that is reserved for one batch in milliseconds. Each second batch is 
	 * used for mining cyclic/acyclic rules. 
	 */'''
  batch_time = 50
  '''/**
	 * The threshold for the number of correctly prediction within the given training set.
	 */'''
  threshold_correct_predictions = 5

  '''/**
	 * The threshold for the confidences.
	 */'''
  threshold_confidence = 0.05