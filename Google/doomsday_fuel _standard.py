import fractions
def lcm(a):
    lcm = a[0]
    for i in a[1:]:
      lcm = lcm*i//fractions.gcd(lcm, i)
    return lcm
def mul(m1, m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1)):
            m3[i].append(sum([m1[i][k]*m2[k][j] for k in range(len(m1))]))
    return m3
def answer(matrix):
    finalStates = []
    sums = []
    for i in range(len(matrix)):
        ss = float(sum(matrix[i]))
        sums.append(ss)
        if ss > 0:
            matrix[i] = [j/ss for j in matrix[i]]
        else:
            matrix[i][i] = 1
            finalStates.append(i)
    m = matrix
    summ = [i for i in range(len(m)) if i not in finalStates]
    while sum(m[0][i] for i in summ) > 0.000000001:
        m = mul(m, matrix)
    fracs = [fractions.Fraction(m[0][i]).limit_denominator()
             for i in finalStates]
    numers = [f.numerator for f in fracs]
    denoms = [f.denominator for f in fracs]
    lc = lcm(denoms)
    numers = [numers[i]*lc//denoms[i] for i in range(len(numers))]
    numers.append(lc)
    return numers
##m = [[0,1,1,0],
##     [0,0,0,0],
##     [0,0,0,0],
##     [0,0,0,0]]

m = [[0, 1, 0, 0, 0, 1],
     [4, 0, 0, 3, 2, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

##m = [[1, 2, 3, 0, 0, 0],
##    [4, 5, 6, 0, 0, 0],
##    [7, 8, 9, 1, 0, 0],
##    [0, 0, 0, 0, 1, 2],
##    [0, 0, 0, 0, 0, 0],
##    [0, 0, 0, 0, 0, 0]]

##m = [[0, 2, 1, 0, 0],
##     [0, 0, 0, 3, 4],
##     [0, 0, 0, 0, 0],
##     [0, 0, 0, 0, 0],
##     [0, 0, 0, 0, 0]]
    
##m = [[0, 2, 1, 0, 3, 2, 1, 6, 7, 3],
##     [1, 0, 0, 3, 4, 2, 1, 4, 5, 2],
##     [1, 1, 1, 1, 0, 6, 3, 4, 8, 7],
##     [0, 3, 0, 1, 0, 3, 2, 1, 3, 8],
##     [3, 0, 4, 0, 1, 2, 3, 1, 5, 2],
##     [0, 3, 0, 1, 0, 3, 2, 1, 3, 8],
##     [0, 3, 0, 1, 0, 3, 2, 1, 3, 8],
##     [0, 3, 0, 1, 0, 3, 2, 1, 3, 8],
##     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
##     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

##m = [[0]]

a = answer(m)
print(a)
