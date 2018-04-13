#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def maxValue(t):
    if (t == None):
        return None
    if (t.right == None):
        return t.value
    return maxValue(t.right)
def deleteNode(t, query):
    if (t == None):
        return None
    if (query == t.value):
        if (t.left == None):
            t = t.right
        else: # t.left != None
            t.value = maxValue(t.left)
            t.left = deleteNode(t.left, t.value)
    elif (query > t.value):
        t.right = deleteNode(t.right, query)
    elif (query < t.value):
        t.left = deleteNode(t.left, query)
    return t
def deleteFromBST(t, queries):
    for query in queries:
        t = deleteNode(t,query)
    return t
