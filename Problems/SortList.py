# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:                
        tempList = []
        
        while head:
            tempList.append(head.val)
            head = head.next
            
        tempList.sort()
        
        result = current = ListNode(0)
        
        for i in tempList:
            current.next=ListNode(i)
            current=current.next
            
        return result.next
