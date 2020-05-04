# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lpreorder = []
        self.treepath(root, lpreorder)
        return lpreorder

    def treepath(self, root, lpreorder):
        if root == None:
            return
        lpreorder.append(root.val)
        self.treepath(root.left, lpreorder)
        self.treepath(root.right,lpreorder)
