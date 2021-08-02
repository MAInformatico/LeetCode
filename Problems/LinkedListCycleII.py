# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pointer1, pointer2 = head, head
        while pointer2 and pointer2.next:
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next
            if pointer2 == pointer1:
                break
        if not pointer2 or not pointer2.next:
            return None
        pointer1 = head
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer2
        
