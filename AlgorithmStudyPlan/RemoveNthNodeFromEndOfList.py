# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        it = head
        
        while n:
            head = head.next
            n -= 1
            
        if not head:
            return it.next
                
        n = it
        while head and head.next:
            head = head.next
            n = n.next
            
        n.next = n.next.next
        return it
    
