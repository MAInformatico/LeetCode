/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if(head == null || head.next == null){
        return head;
    }
    let aux = new ListNode(0);
    aux.next = head;
    let current = aux;
    while(current.next != null && current.next.val != null){        
            let local1 = current.next;
            let local2 = current.next.next
            current.next = local2;
            local1.next = local2.next;
            local2.next = local1;
            current = current.next.next;        
        }    
    return aux.next; 
};
