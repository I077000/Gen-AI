# Function as a Parameter of Another Function

from cmath import pi
import math


def add(a,b):
    return a+b
def doSomething(f,x,y):
    return f(x,y)
print(doSomething(add,3,7))
print(pow(2,2))
print(pi)