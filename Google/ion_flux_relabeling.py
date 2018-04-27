def helper(x, size, q, d):
    # The children of a node x are:
    #  x - 1 and x - (size of subtree x) - 1.
    if size > 1: # if we have not reached bottom of tree
        halfSize = int(size/2)
        right = x - 1
        left = x - halfSize - 1
        # check if current node's children are queried
        if left in q:
            d[left] = x
        if right in q:
            d[right] = x

        # partition q into two parts
        qL = [i for i in q if i <= left] # nodes in left tree
        qR = [i for i in q if i > left] # nodes in right tree
        # we can further trim these, but this is enough to pass the test
        if qL:
            helper(left, halfSize, qL, d)
        if qR:
            helper(right, halfSize, qR, d)
def answer(h, q):
    treeSize = pow(2,h) - 1
    d = {}
    helper(treeSize, treeSize, q, d)
    return [d[x] if x in d else -1 for x in q]
a = answer(30, [1,4,7,1073741822])
print(a)
