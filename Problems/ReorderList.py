# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        pointer = head
        dQueue = deque()
        
        while pointer:
            dQueue.append(pointer)
            pointer = pointer.next
        pointer = None

        while dQueue:
            iter1 = dQueue.popleft()
            iter2 = None if not dQueue else dQueue.pop()

            if iter2: iter2.next = None
            iter1.next = iter2
            
            if pointer: pointer.next = iter1
            pointer = iter2     
        
