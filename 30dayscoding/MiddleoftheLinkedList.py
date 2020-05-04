class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        firstp = secondp = head #two "pointers"
        while secondp and secondp.next:
            firstp = firstp.next
            secondp = secondp.next.next
        return firstp
