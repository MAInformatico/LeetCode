# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        aux = head
        length = 0
        while aux:
            aux = aux.next
            length += 1
        
        previous = target = ListNode(0, head)
        for _ in range(length // k):
            start = previous
            for _ in range(k):
                head.next, head, previous = previous, head.next, head
            start.next.next = head
            start.next, previous = previous, start.next
        
        return target.next
