# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
                
        begin = end = head
        for i in range(1,k):
            begin = begin.next
        
        check = begin
        
        while check.next:
            end = end.next
            check = check.next
                       
        aux = begin.val
        begin.val = end.val
        end.val = aux
        
        return head
    
