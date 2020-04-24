# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        lpreorder = []
        self.treepath(root, lpreorder)
        return lpreorder

    def treepath(self, root, lpreorder):
        if root == None:
            return
        self.treepath(root.left, lpreorder)                  
        self.treepath(root.right,lpreorder)
        lpreorder.append(root.val)        
