# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        checked = True
        
        def review(node, notLessThan, notGreaterThan):
            nonlocal checked #https://docs.python.org/3/reference/simple_stmts.html
            
            if notLessThan and node.val < notLessThan.val:
                node.val, notLessThan.val = notLessThan.val, node.val
                checked = True                
            if notGreaterThan and node.val > notGreaterThan.val:
                node.val, notGreaterThan.val = notGreaterThan.val, node.val
                checked = True                
            if not checked and node.left: review(node.left, notLessThan, node)
            if not checked and node.right: review(node.right, node, notGreaterThan)
        
        while checked:                
            checked = False
            review(root, None, None)
