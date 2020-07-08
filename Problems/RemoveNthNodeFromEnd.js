/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

var removeNthFromEnd = function(head, n) {
    if(!head) return head;
    let result = { val: -1, next: head }
       
    let [pt1, pt2] = [result, result] //two "pointers"
    while(n--){
        pt2 = pt2.next
    }
    
    while(pt2.next){
        [pt1, pt2] = [pt1.next, pt2.next]
    }
    
    pt1.next = pt1.next.next
    
    return result.next
};
