# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(0,len(preorder)-1,preorder)
    
    def buildTree(self,start,end,preorder):
        if start > end:
            return
            
        root = TreeNode(preorder[start])
        i = pre_start
            
        while i<= pre_end:
            if preorder[i] > preorder[start]:
                break
            i+=1
            
        root.left = self.buildTree(start+1,i-1,preorder)
        root.right = self.buildTree(i,end,preorder)
        return root
