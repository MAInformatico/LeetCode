# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        auxList = []
        while head:
            auxList.append(head.val)
            head = head.next
        auxList = auxList[:left-1] + auxList[left-1:right][::-1] + auxList[right:]
        result = temp = ListNode()
        for i in auxList:
            temp.next = ListNode(i)
            temp = temp.next
        return result.next
