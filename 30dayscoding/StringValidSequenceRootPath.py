# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        size = len(arr)
        iterator = 0
        return self.checkPath(root,arr,size,iterator)
    
    def checkPath(self,root,arr,size,iterator):
        if root is None:
            return size == 0
        if (iterator == size-1) and (root.left == None and root.right == None) and (root.val == arr[iterator]):
            return True
        
        if(iterator<size) and (root.val == arr[iterator]):
            return (self.checkPath(root.left,arr,size,iterator+1) or (self.checkPath(root.right,arr,size,iterator+1)))
