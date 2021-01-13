from typing import Tuple
from scratch.linear_algebra import Vector
from scratch.statistics import correlation, standard_deviation, mean, de_mean



def least_squares_fit(x,y):
    beta = correlation(x,y)*standard_deviation(y)/standard_deviation(x)
    alpha = mean(y)-beta*mean(x)
    return alpha, beta


x = [i for i in range(-100,110,10)]
y = [3*i-5 for i in x]


print(de_mean([1,2,3,4,5]))
print("x :",x)
print("y :",y)
print(least_squares_fit(x,y))