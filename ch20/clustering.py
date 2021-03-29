from scratch.linear_algebra import Vector

def num_differences(v1, v2):
    assert len(v1) == len(v2)
    return len([x1 for x1, x2 in zip(v1,v2) if x1 != x2])

assert num_differences([1,2,3],[2,1,3]) == 2

from typing import List
from scratch.linear_algebra import vector_mean

def cluster_means(k, inputs, assignments):
    clusters = [[] for i in range(k)]
    for input,assignment in zip(inputs, assignments):
        clusters[assignment].append(input)

    return [vector_mean(cluster) if cluster else random.choice(inputs) for cluster in clusters]

import itertools
import random
import tqdm
from scratch.linear_algebra import squared_distance

class KMeans:
    def __init__(self, k):
        self.k = k
        self.means = None

    def classify(self, input):
        return min(range(self.k),key=lambda i: squared_distance(input,self.means[i]))

    def train(self, inputs):
        assignments = [random.randrange(self.k) for _ in inputs]

        with tqdm.tqdm(itertools.count()) as t:
            for _ in t:
                self.means = cluster_means(self.k,inputs,assignments)
                new_assignments = [self.classify(input)for input in inputs]

                num_changed = num_differences(assignments,new_assignments)
                if num_changed==0:
                    return

                assignments=new_assignments
                self.means = cluster_means(self.k,inputs,assignments)
                t.set_description(f"changed: {num_changed}/{len(inputs)}")


random.seed(12)
clusterer = KMeans(k=3)
clusterer.train(inputs)
means = sorted(clusterer.means)
