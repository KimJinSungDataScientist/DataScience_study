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

# pip install pillow

image_path = r"k_means_girl.jpeg"
import matplotlib.image as mpimg
img = mpimg.imread(image_path)/256

top_row = img[0]
top_left_pixel = top_row[0]
red,green,blue = top_left_pixel

pixels = [pixel.tolist() for row in img for pixel in row]

clusterer = KMeans(5)
clusterer.train(pixels)

def recolor(pixel):
    cluster = clusterer.classify(pixel)
    return clusterer.means[cluster]
new_img = [[recolor(pixel) for pixel in row]
           for row in img]

import matplotlib.pyplot as plt

plt.imshow(new_img)
plt.axis('off')
plt.show()



################## 상향식 접근 방법 #######################
