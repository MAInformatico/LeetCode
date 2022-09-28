# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0,head)
        pointer = result
        nextPointer = result.next
        
        while nextPointer and n > 0:
            nextPointer = nextPointer.next            
            n -= 1
        
        while nextPointer:
            pointer = pointer.next
            nextPointer = nextPointer.next
        
        pointer.next = pointer.next.next
        
        return result.next
