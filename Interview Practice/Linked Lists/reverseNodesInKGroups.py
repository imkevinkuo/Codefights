# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# Note: Your solution should have O(n) time complexity,
# where n is the number of element in l,
# and O(1) additional space complexity.

def reverse(l,k):
    # size test
    p = l
    s = 1
    while s < k:
        if p.next == None:
            return l, p
        s += 1
        p = p.next
    pointer = l
    front = l
    c = 1
    while c < k:
        c += 1
        n = pointer.next
        nn = n.next
        pointer.next = nn
        n.next = front
        front = n
    return front, pointer # returns head and tail
def reverseNodesInKGroups(l, k):
    pointer = l
    c = 0
    finalHead = l
    prevTail = None
    while pointer != None and pointer.next != None:
        head, tail = reverse(pointer,k)
        pointer = tail
        if prevTail == None:
            finalHead = head
            prevTail = tail
        else:
            prevTail.next = head
            prevTail = tail
        pointer = pointer.next
    return finalHead
