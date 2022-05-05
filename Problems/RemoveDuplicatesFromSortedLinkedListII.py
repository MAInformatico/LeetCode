# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        slow, fast = head, head
        while slow:
            fast = slow.next
            if fast == None:
                break
            if slow.val == fast.val:
                while fast and slow.val == fast.val:
                    fast = fast.next
                if previous == None:
                    head = fast
                else:
                    previous.next = fast
            else:
                previous = slow           
            
            slow = fast
            
        return head    
