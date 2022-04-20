from math import ceil

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        result = head
        
        while head.next != None:            
            count += 1
            head = head.next            
        
        for i in range(count//2):
            result = result.next
            
        return result
