# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
        def remove(head: Optional[ListNode], val: int):
            if head == None:
                return None
            if head.val == val:
                return remove(head.next,val)
            elif head.val != val:
                return ListNode(head.val,remove(head.next,val))
        return remove(head,val)
