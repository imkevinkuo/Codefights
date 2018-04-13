# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# Try to solve this task in O(n) time using O(1) additional
# space, where n is the number of elements in l
def printList(l):
    p = l
    while p != None:
        print(p.value, end=' ')
        p = p.next
    print()
def isListPalindrome(l):
    if l == None:
        return True
    if l.next == None:
        return True
    p = l
    p2 = l
    while p2 != None:
        p2 = p2.next
        if p2 != None:
            p2 = p2.next
            p = p.next
    f = p # front
    while p.next != None:
        n = p.next
        nn = p.next.next
        n.next = f
        f = n
        p.next = nn
    h = f
    while l != h:
        if l.value == f.value:
            l = l.next
            f = f.next
        else:
            return False
        if l == None or f == None:
            return True
    return True
