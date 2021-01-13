from scratch.linear_algebra import distance

a_to_b = distance([63,150],[67,160])
a_to_c = distance([63,150],[70,171])
b_to_c = distance([67,160],[70,171])

from typing import Tuple

from scratch.linear_algebra import vector_mean
from scratch.statistics import standard_deviation

def scale(data):
    dim = len(data[0])

    means = vector_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data]) for i in range(dim)]

    return means, stdevs

vectors = [[-3,-1,1],[-1,0,1],[1,1,1]]
means, stdevs = scale(vectors)

assert means == [-1,0,1]
assert stdevs == [2,1,0]

def rescale(data):
    dim = len(data[0])
    means, stdevs = scale(data)

    rescaled = [v[:] for v in data]

    for v in rescaled:
        for i in range(dim):
            if stdevs[i]>0:
                v[i] = (v[i] - means[i]) / stdevs[i]

    return rescaled

means, stdevs = scale(rescale(vectors))
assert means == [0,0,1]
assert stdevs == [1,1,0]