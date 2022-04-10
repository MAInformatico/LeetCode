# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checker(root, leftBranch, rightBranch):
            if not root:
                return True
            
            if leftBranch < root.val < rightBranch:
                return (checker(root.left, leftBranch, root.val) and checker(root.right, root.val, rightBranch))
            
            return False                
        
        return checker(root, float('-inf'), float('inf'))
