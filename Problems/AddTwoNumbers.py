# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        elif not l2:
            return l1
        
        result = iterator = ListNode(0)
        decimal, sum = 0, 0
                       
        while l1 or l2:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            sum += decimal
            
            iterator.next = ListNode(sum % 10)
            decimal = sum // 10
            iterator = iterator.next
            sum = 0
        
        if(decimal):
            iterator.next = ListNode(decimal)
            
        return result.next
