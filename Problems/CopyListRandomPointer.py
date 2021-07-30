"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head==None:
            return head
        
        result=Node(head.val)
        temp=head.next
        aux=result
        while(temp):
            aux.next=Node(temp.val)
            aux=aux.next
            temp=temp.next            
            
        temp=head
        aux=result        
        while(temp):
            next=temp.next
            temp.next=aux
            aux.random=temp.random
            aux=aux.next
            temp=next        
            
        aux=result        
        while(aux):
            if aux.random!=None:
                aux.random=aux.random.next
            aux=aux.next
            
        return result
