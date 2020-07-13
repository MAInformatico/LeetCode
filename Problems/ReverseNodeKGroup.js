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
var reverseKGroup = function(head, k) {
  if (!head || k == 1) return head;

    const result = new ListNode(-1);
    result.next = head;
    let cur = result, pre = result, nxt;
	
    let num = 0;
    while (cur = cur.next) ++num;

    while (num >= k) {
        cur = pre.next;
        nxt = cur.next;
        for (let i = 1; i < k; ++i) {
            cur.next = nxt.next;
            nxt.next = pre.next;
            pre.next = nxt;
            nxt = cur.next;
        }
        pre = cur;
        num -= k;
    }
    return result.next;  
};
