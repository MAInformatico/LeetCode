# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        l = self.checkDepth(root.left) 
        r = self.checkDepth(root.right)
        return (abs(l-r) <2) and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def checkDepth(self,node):
        if node == None: return 0
        return max(self.checkDepth(node.left),self.checkDepth(node.right))+1        
