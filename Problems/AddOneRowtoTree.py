# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left = root)
        
        queue = deque([root])
        height, size = 0, 0
        
        while queue:
            size = len(queue)
            
            while size:
                node = queue.popleft()
                
                if height == depth - 2:
                    aux = node.left
                    node.left = TreeNode(val)
                    node.left.left = aux
                    
                    aux = node.right
                    node.right = TreeNode(val)
                    node.right.right = aux
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                size -= 1
            
            height += 1
        
        return root
