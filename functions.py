from math import *

def sum_squares_function(x):
    return sum([(i+1)*x[i]**2 for i in range(len(x))])

def sum_of_different_powers_function(x):
    return sum([abs(x[i])**(i+2) for i in range(len(x))])

def easom_function(x):
    return -cos(x[0])*cos(x[1])*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)
