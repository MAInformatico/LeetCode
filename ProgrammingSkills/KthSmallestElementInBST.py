# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNumbers(self,root, auxArray):
        if not root:
            return
            
        self.getNumbers(root.left,auxArray)
        auxArray.append(root.val)
        self.getNumbers(root.right,auxArray)    
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        auxArray = []
        self.getNumbers(root,auxArray)
        return auxArray[k-1]
