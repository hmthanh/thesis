class ApplyConfig(object):
  '''**
	 * Returns only results for head or tail computation if the results set has less elements than this bound.
	 * The idea is that any results set which has more elements is anyhow not useful for a top-k ranking. 
	 * Should be set to a value thats higher than the k of the requested top-k (however, the higher the value,
	 * the more runtime is required)
	 * '''
  discrimination_bound = 1000

  '''**
	* Number of maximal attempts to create body grounding. Every partial body grounding is counted.
	*'''
  trial_size = 100000
  '''/**
	 * The number of negative examples for which we assume that they exist, however, we have not seen them. Rules with high coverage are favored the higher the chosen number. 
	*/'''
  unseen_nagative_example = 5	
  '''/**
	 * Defines the prediction type which also influences the usage of the other parameters. 
	 * Possible values are currently aRx and xRy.
	 */
  '''
  prediction_type = 'aRx'
  '''/**
	 * Path to the file that contains the triple set used for learning the rules.
	 */
  '''
  path_training = ''
  '''/**
	 * Path to the file that contains the triple set used for to test the rules.
	 */
  '''
  path_test = ''
  '''/**
	 * Path to the file that contains the triple set used validation purpose (e.g. learning hyper parameter).
	 */'''
  path_valid = ''
  '''/**
	 * The top-k results that are after filtering kept in the results. 
	 */'''
  top_k_output = 10