class Apply(object):
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
	public trial_size = 100000
