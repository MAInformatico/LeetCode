# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def dfs(root, leftBranch):
            if not root:
                return

            if leftBranch and not root.left and not root.right:
                self.result += root.val
            
            dfs(root.left,True)
            dfs(root.right,False)
                        
        dfs(root,False)        
        return self.result
