# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode(carry)
        result = l3
        
        while l1 or l2:
            aux = 0
            if l1:
                aux += l1.val
                l1 = l1.next
            if l2:
                aux += l2.val
                l2 = l2.next
            localSum = (aux + carry)
            l3.next = ListNode(localSum % 10)
            l3 = l3.next
            carry = localSum // 10
        
        if carry != 0:
            l3.next = ListNode(carry)
            l3 = l3.next
        return result.next
