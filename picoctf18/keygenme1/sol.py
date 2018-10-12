import itertools
import string
def _ord(a):
    if ord(a) in range(48,58):
        return ord(a)-48
    return ord(a)-55

def check(s):
    l = len(s)
    v2 = 0
    for i in range(l-1):
        v2 += (_ord(s[i])+1)*(i+1)
    x = (v2%36) - (_ord(s[l-1]))
    return x

s = string.ascii_uppercase + "0123456789"

for comb in itertools.combinations(s, 16):
    if check(''.join(comb)) == 0:
        print(''.join(comb))
        