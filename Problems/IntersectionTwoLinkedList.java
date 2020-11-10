/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public int sizeListNode(ListNode aux){
        int result = 0;
        while(aux != null){
            result++;
            aux = aux.next;
        }
        return result;
    }    
    
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int sizeA = 0;
        int sizeB = 0;
        ListNode aux = headA;
        
        sizeA = sizeListNode(headA);
        sizeB = sizeListNode(headB);
        
        if(sizeA>sizeB)  for(int i=0;i<sizeA-sizeB;i++) headA = headA.next;
        else if(sizeB>sizeA) for(int i=0;i<sizeB-sizeA;i++) headB = headB.next;
        while(headA != headB){
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
}
