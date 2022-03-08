# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        tortoise = head #Floyd's algorithm
        hare = head.next
        while hare.next and hare.next.next and tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise == hare
