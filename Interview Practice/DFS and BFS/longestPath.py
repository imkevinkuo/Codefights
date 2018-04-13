def isFileName(s):
    return '.' in s
def pathLength(a, s):
    t = s.count('\t')
    l = len(s) - t
    print(s, len(s) - t)
    for i in range(a.index(s), -1, -1):
        cS = a[i] # current S
        cT = cS.count('\t')
        print(cS, len(cS) - cT)
        if cT < t:
            l += len(cS) - cT + 1
            t = cT
    return l
def longestPath(fileSystem):
    a = fileSystem.split("\f")
    print(a)
    lengths = [pathLength(a,s) for s in a if isFileName(s)]
    return max(lengths) if len(lengths) > 0 else 0
