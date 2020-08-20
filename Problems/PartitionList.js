/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    const less = new ListNode(), more = new ListNode();
    let itcurr = head, currL = less, currM = more;
    
    while(itcurr) {
        if(itcurr.val < x) currL = currL.next = itcurr;
        else currM = currM.next = itcurr;
        itcurr = itcurr.next;        
    }
    currL.next = more.next;
    currM.next = null;
    return less.next;
};
