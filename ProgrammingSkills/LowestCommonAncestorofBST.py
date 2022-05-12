# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def FindCommonAncestor(root,p,q):
            if not root:
                return None
            if root == p or root == q:
                return root
            
            left = FindCommonAncestor(root.left,p,q)
            right = FindCommonAncestor(root.right,p,q)
            
            if left and right:
                return root
            if not left:
                return right
            
            return left
        
        return FindCommonAncestor(root,p,q)
