# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        aux = ListNode(head.next.val, ListNode(head.val, None))
        
        aux.next.next = self.swapPairs(head.next.next)
        return aux
