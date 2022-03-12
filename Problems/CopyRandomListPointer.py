"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dictionary = {}
        prev, current = None, head
        while current:
            dictionary[current] = copy.copy(current)
            
            if prev:
                dictionary[prev].next = dictionary[current]
            
            prev, current =current, current.next
            
        current = head
        while current:
            if current.random:
                dictionary[current].random = dictionary[current.random]
            current = current.next
        
        return dictionary[head]
