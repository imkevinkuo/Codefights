#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
   if len(inorder) > 0 and len(preorder) > 0:
      root = Tree(preorder[0])
      i = inorder.index(preorder[0])
      root.left = restoreBinaryTree(inorder[:i], preorder[1:1+i])
      root.right = restoreBinaryTree(inorder[i+1:], preorder[1+i:])
      return root
