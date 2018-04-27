import numpy as np
import fractions
from math import gcd
def lcm(a):
    lcm = a[0]
    for i in a[1:]:
      lcm = lcm*i//gcd(lcm, i)
    return lcm
def answer(matrix):
    finalStates = []
    for v in range(len(matrix)):
        s = sum(matrix[v])
        if s > 0:
            matrix[v] = [a/s for a in matrix[v]]
        else:
            matrix[v][v] = 1
            finalStates.append(v)

    matrixT = np.transpose(matrix)
    vec = [0 if i > 0 else 1 for i in range(len(matrix))]
    for i in range(30):
        vec = np.matmul(matrixT, vec)
    fcs = [fractions.Fraction(vec[v]).limit_denominator() for v in finalStates]
    n = [f.numerator for f in fcs]
    d = [f.denominator for f in fcs]
    l = lcm(d)
    final = [n[i]*l//d[i] for i in range(len(fcs))]
    final.append(l)
    return final
m = [[1, 2, 2, 2, 0],
     [2, 1, 2, 1, 4],
     [4, 0, 2, 4, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]
a = answer(m)
print(a)
