# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        next_node = self.removeNodes(node.next)
        
        node.next = next_node
        if not next_node or node.val >= next_node.val:
            return node
        return next_node
