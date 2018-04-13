# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    lsize = 0
    if l != None:
        lsize = 1
        lastNode = l
        while lastNode.next != None:
            lastNode = lastNode.next
            lsize += 1
        if lsize > 1:
            diff = lsize - n
            p2 = l
            if diff == 0:
                return l
            for i in range(diff-1):
                p2 = p2.next
            lastNode.next = l
            newFront = p2.next
            p2.next = None
            return newFront
        return l
