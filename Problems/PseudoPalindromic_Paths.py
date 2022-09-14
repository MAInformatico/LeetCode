# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def DFS(root, bitmap):
            if not root:
                return 0
            bitmap ^= 1 << root.val
            if not root.left and not root.right:
                return int(bitmap & (bitmap - 1) == 0)
            return DFS(root.left, bitmap) + DFS(root.right, bitmap)
        
        return DFS(root, 0)
