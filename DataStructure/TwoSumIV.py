# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def convertToList(node,arr):
            if node != None:
                arr.append(node.val)
                convertToList(node.left,arr)
                convertToList(node.right,arr)
            return
        
        aux = []
        convertToList(root,aux)
        for i in range(0,len(aux)):
            result = False
            for j in range(i+1,len(aux)):
                if aux[i] + aux[j] == k:
                    result = True
                    break
            if result == True:
                break
        return result
