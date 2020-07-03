## 2 Translation-based mod


Given a training set S of triplets $(h, l, t)$ composed of two entities $h, t ∈ E$ (the set of entities) and a
relationship $l ∈ L$ (the set of relationships), our model learns vector embeddings of the entities and
the relationships. The embeddings take values in $\mathbb{R}^k$ (k is a model hyperparameter) and are denoted
with the same letters, in boldface characters. 

**The basic idea behind our model is that the functional relation induced by the $l$-labeled edges corresponds to a translation of the embeddings**
, i.e. we want that $h + l ≈ t$ when $(h, l, t)$ holds ($t$ should be a nearest neighbor of $h + l$), while $h + l$ should be
far away from $t$ otherwise. Following an energy-based framework, the energy of a triplet is equal to $d(h + l, t)$ for some dissimilarity measure $d$, which we take to be either the $L_1$ or the $L_2$-norm.

$d$ : giá trị đo sự khác nhau của $h + l$ so với $t$




![alt text](/img/TransE/TransE_alg.png)

