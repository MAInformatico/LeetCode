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
var insertionSortList = function(head) {
    let linkedList = new ListNode(0);
    let current = head;
    let next = null;
    let aux = null;
    while (current) {
        next = current.next;
        aux = linkedList;
        while (aux.next && aux.next.val < current.val) {
            aux = aux.next;
        }
        current.next = aux.next;
        aux.next = current;
        current = next;
    }
  return linkedList.next;
};
