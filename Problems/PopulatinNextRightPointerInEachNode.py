"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        aux = Node(-999)
        while queue:
            length = len(queue)
            
            previous = aux
            for _ in range(length):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                    previous.next = popped.left
                    previous = previous.next
                if popped.right:
                    queue.append(popped.right)
                    previous.next = popped.right
                    previous = previous.next
                    
        return root
