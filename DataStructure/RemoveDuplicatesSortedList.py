# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        currentNode = head
        nextNode = currentNode.next if currentNode is not None else None
        
        while nextNode is not None:
            if currentNode.val == nextNode.val:
                currentNode.next = nextNode.next
            
            else:
                currentNode = currentNode.next
            
            nextNode = nextNode.next
        
        return head
