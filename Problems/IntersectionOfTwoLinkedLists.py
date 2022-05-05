# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        iterA = headA
        iterB = headB
        while iterA != iterB:
            if iterA:
                iterA = iterA.next
            else:
                iterA = headB
            
            if iterB:
                iterB = iterB.next
            else:
                iterB = headA
            
            
        return iterA
