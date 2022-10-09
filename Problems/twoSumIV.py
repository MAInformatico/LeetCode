# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dictionary = dict()
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        
        if k-root.val in self.dictionary:
            return True
        
        self.dictionary[root.val] = None
        
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)            
