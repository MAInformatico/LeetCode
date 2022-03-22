"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
                
        def dfs(root):
            if not root: return None
            
            left = dfs(root.left)
            right = dfs(root.right)
                        
            if left and right: 
                left.next = right
                right.next = None
                
                auxLeft = left.right
                auxRight = right.left
                while auxLeft and auxRight:
                    auxLeft.next = auxRight
                    auxLeft = auxLeft.right
                    auxRight = auxRight.left
                return root
            
            else: return root
            
        return dfs(root)
