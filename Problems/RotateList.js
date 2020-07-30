/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
  if (head === null) 
        return head; 

    let tmp = head; 
    let len = 1; //get head size
    while (tmp.next != null) { 
        tmp = tmp.next; 
        len++; 
    } 
  
    if (k > len) 
        k = k % len; 
  
    k = len - k; 

    if (k === 0 || k === len) 
        return head; 

    let current = head; 
    let count = 1; 
    while (count < k && current != null) { 
        current = current.next; 
        count++; 
    } 
  
    if (current == null) 
        return head; 
  
    let kthnode = current; 
  
    tmp.next = head; 
  
    head = kthnode.next; 
  
    kthnode.next = null; 
  
    return head;   
};
