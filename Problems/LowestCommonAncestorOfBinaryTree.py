# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def backtrack(node,p,q):
            if node==p or node==q or node==None:
                return node
            
            leftChild=backtrack(node.left,p,q)
            rightChild=backtrack(node.right,p,q)
            
            if leftChild==None:
                return rightChild
            
            elif rightChild==None:
                return leftChild
            
            else:
                return node
        
        return backtrack(root,p,q)
