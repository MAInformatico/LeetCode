# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return

        if (root.left is None) and (root.right is None):
            return root

        pl, pr = None, None

        if root.left:
            pl = self.flatten(root.left)

        if root.right:
            pr = self.flatten(root.right)

        aux = root.right

        if pl:
            root.right = root.left
            pl.right = aux

        root.left = None

        return pr or pl
