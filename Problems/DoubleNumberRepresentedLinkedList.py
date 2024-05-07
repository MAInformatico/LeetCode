# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calculate_double(node):
            if not node:
                return 0

            new_value = node.val * 2 + calculate_double(node.next)
            node.val = new_value % 10
            return new_value // 10

        carry = calculate_double(head)

        if carry:
            result = ListNode(carry)
            result.next = head
            return result
        
        return head
