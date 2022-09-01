# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maximum = root.val
        result = 0
        def DFS(node,maximum):
            nonlocal result
            if not node:
                return
            if node:
                if node.val >= maximum:
                    maximum = node.val
                    result += 1
            DFS(node.left,maximum)
            DFS(node.right,maximum)
        DFS(root,root.val)
        return result
