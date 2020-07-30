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
    const checker = (curr, prev) => {
        if (curr === null)  return;        
        
        if (prev && prev.val === curr.val) {
            prev.next = curr.next;
            checker(curr.next, prev);    
        }
        else {
            checker(curr.next, curr);    
        }
    }
    checker(head, null);
    return head;
};
