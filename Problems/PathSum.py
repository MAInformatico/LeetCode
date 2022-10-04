# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(current, currentSum=0):
            if current is None:
                return False
            
            currentSum += current.val
            
            if not current.left and not current.right and currentSum == targetSum:
                return True
            
            return DFS(current.left, currentSum) or DFS(current.right, currentSum)
        
        return DFS(root)
