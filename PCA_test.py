from scratch.linear_algebra import subtract
from scratch.linear_algebra import vector_mean

def de_mean(data): #평균 0 으로 만들어버림
    mean = vector_mean(data)
    return [subtract(vector, mean) for vector in data]

from scratch.linear_algebra import magnitude

def direction(w):
    mag = magnitude(w) #magnitude는 평균값으로부터 거리가 0이라는 전제 하에 사용할 수 있을듯
    return [w_i / mag for w_i in w]
