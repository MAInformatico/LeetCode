# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = self.result = 0
        
        def checkChild(node):
            if not node:
                return
            
            checkChild(node.left)
            
            self.count += 1     
            if self.count == k:
                self.result = node.val
                return
            
            checkChild(node.right)
        
        checkChild(root)
        return self.result
