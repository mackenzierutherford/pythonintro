# hw9pr3.py
# Mackenzie Rutherford

import random

def throwDart():
    """Throws one "dart" at a random place in the square between 
        -1 and 1, returns True if dart hits circle and False if it does not
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
        return True
    else:
        return False
    
def forPi(N):
    """Accepts an integer N for number of throws and throw darts
    at center of square, returning the number of hits and the value
    of pi
    """
    numhits = 0.0
    numthrows = 0.0
    for x in range(N):
        if throwDart():
            numhits += 1.0
        numthrows += 1.0
        print(numhits, "hits out of", numthrows, "throws so that pi is", numhits*4.0/(numthrows))
    return 4.0 * numhits / N

import math

def whilePi(error):
    """accepts a positive floating point value, error. Returns 
        the absolute difference between the function's estimate of pi
        and the real value of pi is less than error.
    """
    numhits = 0.0
    numthrows = 0.0
    estpi = 4.0
    while abs(estpi - math.pi) > error:
        if throwDart():
            numhits += 1.0
        numthrows += 1.0
        estpi = 4.0*numhits/numthrows
        print(numhits, "hits out of", numthrows, "throws so that pi is", estpi)
    return numthrows