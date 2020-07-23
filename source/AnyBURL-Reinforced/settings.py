import yaml

class Settings(object):

  def __init__(self):
    '''*
    * Do not change this. For APPLY its required that this is set to false, for LEARNING both is okay
    *'''
    self.REWRITE_REFLEXIV = False
    self.REWRITE_REFLEXIV_TOKEN = 'me_myself_i'
    self.BEAM_NOT_DFS = True
    self.BEAM_TYPE_EDIS = True
    '''
    * Suppresses any rules with constants.
    *'''
    self.CONSTANTS_OFF = False
    self.EPSILON = 0.1
    '''
    **
    * In the first batch the decisions are completely randomized. This random influence becomes less
    * at will be stable at  RANDOMIZED_DECISIONS after this number of batches have been carried out.
    **
    '''
    self.RANDOMIZED_DECISIONS_ANNEALING = 5
    '''
    * This number defines if a rule to be redundant if the number of groundings for its last atom is less than this parameter.
    * It avoid that rules with constants are too specific and thus redundant compared to shorter rules 
    *    head(X,c) <= hasGender(X, female)
    *    head(X,c) <= hasGender(X, A), hasGender(berta, A)
    * The second rule will be filtered out, because berta has only 1 gender, which is female.
    '''
    self.AC_MIN_NUM_OF_LAST_ATOM_GROUNDINGS = 5
    '''
    * PROBABLY OUT 
    * 
    * The specialization confidence interval determines that a rule shall only be accepted as a specialization of a more general rule, if
    * it has a higher confidence and if the probability that its confidence is really higher is at least that chosen value.
    * Possible values are 0.9, 0.99 and 0.99.
    * 
    * -1 = turned-off
    '''
    self.SPECIALIZATION_CI = -1
    '''
    * Relevant for reinforced learning, how to compute the scores created by a thread.
    * 
    * 1 = correct predictions
    * 2 = correct predictions weighted by confidence
    * 3 = correct predictions weighted by applied confidence
    * 4 = correct predictions weighted by applied confidence^2
    * 5 = correct predictions weighted by applied confidence divided by (rule length-1)^2
    '''
    self.REWARD = 5
    '''
    * Relevant for reinforced learning, how to use the scores created by a thread within the decision.
    * 
    * 1 = GREEDY = Epsilon greedy: Focus only on the best.
    * 2 = WEIGHTED = Weighted policy: focus as much as much a a path type, as much as it gave you.
    '''
    self.POLICY = 2
    self.SCORING_REGIME_CONFDIFF = 0.0
    '''
    * Defines the prediction type which also influences the usage of the other parameters. 
    * Possible values are currently aRx and xRy.
    '''
    self.PREDICTION_TYPE = 'aRx'
    '''
    * Path to the file that contains the triple set used for learning the rules.
    '''
    self.path_training = ''
    '''
    * Path to the file that contains the a triple set that has been materialized by applying some rule set to a training set.
    * This set is used in the prediction phase as additional input, however, its not used for filtering to avoid that
    * triples that are 'again' derived are suppressed.
    '''
    self.PATH_MATERIALIZED = ''
    '''
    * Path to the file that contains the triple set used for to test the rules.
    '''
    self.PATH_TEST = ''
    '''
    * Path to the file that contains the triple set used validation purpose (e.g. learning hyper parameter).
    '''
    self.PATH_VALID = ''
    '''
    * Path to the file that contains the rules that will be refined or will be sued for prediction.
    '''
    self.PATH_RULES = ''
    '''
    * Path to the file that contains the rules that will be used as base,
    * i.e. this rule set will be added to all other rule sets loaded.
    '''
    self.PATH_RULES_BASE = ''
    '''
    * Path to the output file where the rules / predictions  will be stored.
    '''
    self.path_output = ''
    '''
    * Path to the output file where statistics of the dice are stored.
    * Can be used in reinforcement learning only. If the null value is not overwritten, nothing is stored.
    '''
    self.PATH_DICE = ''

    '''
    * Path to the output file where the explanations are stored. If not set no explanations are stored.
    '''
    self.PATH_EXPLANATION = None

    self.EXPLANATION_WRITER = None
    '''
    * Takes a snapshot of the rules refined after each time interval specified in seconds.
    '''
    self.snapshots_at = [10, 100]
    '''
    * Number of maximal attempts to create body grounding. Every partial body grounding is counted.
    * 
    * NO LONGER IN USE (maybe)
    '''
    self.TRIAL_SIZE = 1000000
    '''
    * Returns only results for head or tail computation if the results set has less elements than this bound.
    * The idea is that any results set which has more elements is anyhow not useful for a top-k ranking. 
    * Should be set to a value thats higher than the k of the requested top-k (however, the higher the value,
    * the more runtime is required)
    * 
    * PROBABLY OUT ... no its in again
    '''
    self.DISCRIMINATION_BOUND = 1000
    '''
    * The time that is reserved for one batch in milliseconds. 
    '''
    self.BATCH_TIME = 1000
    '''
    * The maximal number of body atoms in cyclic rules (inclusive this number). If this number is exceeded all computation time
    * is used for acyclic rules only from that time on.
    '''
    self.MAX_LENGTH_CYCLIC = 3
    '''
    * The maximal number of body atoms in acyclic rules (inclusive this number). If this number is exceeded all computation time
    * is used for cyclic rules only from that time on.
    '''
    self.MAX_LENGTH_ACYCLIC = 1

    '''
    * The maximal number of body atoms in partially grounded cyclic rules (inclusive this number). If this number is exceeded than a
    * cyclic path that would allow to construct such a rule (where the constant in the head and in the body is the same) is used for constructing
    * general rules only, partially grounded rules are not constructed from such a path.
    '''
    self.MAX_LENGTH_GROUNDED_CYCLIC = 1
    '''
    * The threshold for the number of correct prediction created with the refined rule.
    '''
    self.THRESHOLD_CORRECT_PREDICTIONS = 2
    '''
    * The threshold for the number of correct predictions. Determines which rules are read from a file and which are ignored.
    '''
    self.RR_THRESHOLD_CORRECT_PREDICTIONS = 2
    '''
    *The number of negative examples for which we assume that they exist, however, we have not seen them. Rules with high coverage are favored the higher the chosen number. 
    '''
    self.UNSEEN_NEGATIVE_EXAMPLES = 5
    '''
    * The number of negative examples for which we assume that they exist, however, we have not seen them.
    * This number is for each refinements step, including the refinement of a refined rule.
    '''
    self.UNSEEN_NEGATIVE_EXAMPLES_REFINE = 5
    '''
    * These number are added rule specific for in the application phase.
    *                      
    *                         U   C  AC1 AC2  X
    '''
    self.UNSEEN_NEGATIVE_EXAMPLES_ATYPED = [0, 0, 0, 0, 0]
    '''
    * If set to true, the rule application is done on the rule set and each subset that consists of one type as well as each subset that removed one type.
    * This setting should be used in an ablation study.
    '''
    self.TYPE_SPLIT_ANALYSIS = False

    '''
    * The threshold for the confidence of the refined rule
    '''
    self.THRESHOLD_CONFIDENCE = 1e-4
    '''
    * The threshold for the confidence of the rule. Determines which rules are read from a file by the rule reader.
    '''
    self.RR_THRESHOLD_CONFIDENCE = 1e-4
    '''
    * The number of worker threads which compute the scores of the constructed rules, should be one less then the number of available cores.
    '''
    self.worker_threads = 3
    '''
    * Defines how to combine probabilities that come from different rules
    * Possible values are: maxplus, noisyor
    '''
    self.AGGREGATION_TYPE = 'maxplus'
    '''
    * This value is overwritten by the choice made vie the AGGREGATION_TYPE parameter
    '''
    self.AGGREGATION_ID = 1

    '''
    * No longer intended to be overwritten by properties file.
    * Is automatically set by inspecting the validation set comparing it to the training set.
    '''
    self.PREDICT_ONLY_UNCONNECTED = False
    '''
    * Used for restricting the number of samples drawn for computing scores as confidence.
    '''
    self.SAMPLE_SIZE = 2000
    '''
    * The maximal number of body groundings. Once this number of body groundings has been reached,
    * the sampling process stops and confidence score is computed.
    '''
    self.BEAM_SAMPLING_MAX_BODY_GROUNDINGS = 1000
    '''
    * The maximal number of attempts to create a body grounding. Once this number of attempts has been reached
    * the sampling process stops and confidence score is computed.
    '''
    self.BEAM_SAMPLING_MAX_BODY_GROUNDING_ATTEMPTS = 100000
    '''
    * If a rule has only few different body groundings this parameter prevents that all attempts are conducted.
    * The value of this parameter determines how often a same grounding is drawn, before the sampling process stops
    * and the and confidence score is computed, e.g, 5 means that the algorithm stops if 5 times a grounding is
    * constructed tat has been found previously. The higher the value the mor probably it is that the sampling
    * computes the correct value for rules with few body groundings.
    '''
    self.BEAM_SAMPLING_MAX_REPETITIONS = 5
    '''
    * The top-k results that are after filtering kept in the results. 
    '''
    self.TOP_K_OUTPUT = 10

    self.READ_CYCLIC_RULES = 1
    self.READ_ACYCLIC1_RULES = 1
    self.READ_ACYCLIC2_RULES = 1

    self.KEYWORD = {'greedy': 1, 'weighted': 2, 'sup': 1, 'supXcon': 3, 'supXcon/lr': 5, 'supXcon/rl': 5}

  def load_laerning_config(self):
    with open('learning.yaml') as stream:
    # use safe_load instead load
      conf = yaml.safe_load(stream)
      self.path_training = conf['PATH_TRAINING']
      self.path_output = conf['PATH_OUTPUT']
      self.snapshots_at = conf['SNAPSHOTS_AT']
      self.worker_threads = conf['WORKER_THREADS']