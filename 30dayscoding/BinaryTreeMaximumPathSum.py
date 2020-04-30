# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')
        def get_sum(root):
            if root is None:
                return 0
            else:
                leftbranch = max(get_sum(root.left), 0)
                rightbranch = max(get_sum(root.right), 0)
                self.max = max(self.max, leftbranch + rightbranch + root.val)
                return max(leftbranch, rightbranch, 0) + root.val
        
        get_sum(root)
        return self.max
