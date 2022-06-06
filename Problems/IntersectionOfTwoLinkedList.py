# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        iter1 = headA
        iter2 = headB
        
        while iter1 != iter2:
            iter1 = iter1.next if iter1 else headB
            iter2 = iter2.next if iter2 else headA
        return iter1
