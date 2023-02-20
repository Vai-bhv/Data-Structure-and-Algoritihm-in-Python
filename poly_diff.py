import collections 
import itertools
from math import fabs
import sys
coefficients1 = []
coefficients2 = []
operation = sys.stdin.readline().strip("\n")
while True:
    inp = sys.stdin.readline().split(" ")
    inpu = [v for v in inp if v != ""]
    inpu = [int(x) for x in inpu]
    if inpu[0] == inpu[1] == -1:
         break
    else:
        coefficients1.append((inpu[0], inpu[1]))

while True:
    inp = sys.stdin.readline().split(" ")
    inpu = [v for v in inp if v != ""]
    inpu = [int(x) for x in inpu]
    if inpu[0] == inpu[1] == -1:
         break
    else:
        coefficients2.append((inpu[0], inpu[1]))


def counter_to_poly(c):
    p = [(exp, coeff) for exp, coeff in c.items() if coeff != 0]
    p.sort(key = lambda pair: pair[0], reverse = True)
    return p


def div(p, q):
    pass 

def add(p, q):
    r = collections.Counter()

    for e, c in (p + q):
        r[e] += c

    return counter_to_poly(r)

def mul(p, q):
    r = collections.Counter()

    for (e1, c1), (e2, c2) in itertools.product(p, q):
        r[e1 + e2] += c1 * c2

    return counter_to_poly(r)
result = ""
if (operation == 'add'):
    result = add(coefficients1, coefficients2)
    
elif (operation == 'mul'):
    result = mul(coefficients1,coefficients2)

for kk in result:
    print("{} {}".format(kk[0], kk[1]))
print("-1 -1")


