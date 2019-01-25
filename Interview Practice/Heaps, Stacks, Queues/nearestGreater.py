def nextLarger(a):
    stack = []
    newLis = [-1 for n in a]
    for i in range(1, len(a)):
        stack.append((a[i-1], i-1)) # val, index
        if a[i-1] < a[i]:
            while len(stack) > 0 and stack[-1][0] < a[i]:
                s = stack.pop()
                newLis[s[1]] = i
    return newLis
def nearestGreater(a):
    fwd = nextLarger(a)
    bwd = [len(a) - 1 - b if b > -1 else -1 for b in nextLarger(a[::-1])[::-1]]
    newLis = [-1 for i in a]
    for i in range(len(a)):
        if fwd[i] > -1 and bwd[i] > -1:
            f = abs(i-fwd[i]) #distances
            b = abs(i-bwd[i])
            if f == b or f > b:
                newLis[i] = bwd[i]
            elif b > f:
                newLis[i] = fwd[i]
        elif fwd[i] > -1:
            newLis[i] = fwd[i]
        elif bwd[i] > -1:
            newLis[i] = bwd[i]
        
    return newLis
