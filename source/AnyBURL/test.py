from data.triple_set import TripleSet

data = TripleSet()
data.read_triples('../../datasets/FB15k-237/test.txt')

'\n'.join([str(item) for item in data.triples[0:10]])