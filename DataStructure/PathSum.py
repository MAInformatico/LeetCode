# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        checker = [False]
        
        def dfs(tree, num):
            if not tree:
                return
            
            if tree.left is None and tree.right is None:
                if tree.val + num == targetSum:
                    checker[0] = True
        
            dfs(tree.left, num + tree.val)
            dfs(tree.right, num + tree.val)
            
        dfs(root,0)
        return checker[0]
