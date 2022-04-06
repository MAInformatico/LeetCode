# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lpreorder = []
        self.treepath(root, lpreorder)
        return lpreorder

    def treepath(self, root, lpreorder):
        if root == None:
            return
        self.treepath(root.left, lpreorder)
        lpreorder.append(root.val)        
        self.treepath(root.right,lpreorder)
