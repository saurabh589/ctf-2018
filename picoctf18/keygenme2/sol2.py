from z3 import *
import itertools
import string
def _ord(a):
    if ord(a) in range(48,58):
        return ord(a)-48
    return ord(a)-55

def mod(x,y):
    if x % y >= 0:
        result = x%y
    else:
        result = x%y + y
    return result


s = string.ascii_uppercase + "0123456789"

x = Int('x')
y  =Int('y')
s = Solver()
s.add()
s.add(mod(x+y,36)==14)
for c in s.assertions():
    print c

