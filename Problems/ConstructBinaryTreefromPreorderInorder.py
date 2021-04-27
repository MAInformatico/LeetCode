# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        index = inorder.index(preorder.pop(0))
        currentNode = TreeNode(inorder[index])
        
        currentNode.left = self.buildTree(preorder, inorder[:index])
        currentNode.right = self.buildTree(preorder, inorder[index+1:])
     
        return currentNode
