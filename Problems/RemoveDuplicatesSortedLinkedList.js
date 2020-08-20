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
var deleteDuplicates = function(head) {
    let itcurr = head;
    let prev;
    let repeated = null;
    head = null;
    while(itcurr){
        if(itcurr.next !== null && itcurr.val === itcurr.next.val){ //remove duplicate
            repeated = itcurr.val;
            itcurr = itcurr.next;
            if (prev) prev.next = null;
        }
        else{ //continue iterating
            if (itcurr.val !== repeated){
                if(!head) head = itcurr;
                else prev.next = itcurr;
                prev = itcurr;
            }
            itcurr = itcurr.next;
        }
    }    
    return head;
};
