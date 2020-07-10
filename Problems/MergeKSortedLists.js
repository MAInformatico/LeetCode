/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

var mergeKLists = function(lists) {    
    let nodes = [];
    lists.forEach((list) => {
        while (list) {
            nodes.push(list);
            list = list.next;
        }
    })
    
    if (nodes.length === 0) return null;
    
    nodes.sort((a, b) => a.val - b.val);
    
    for (let i = 0; i < nodes.length; i++) {
        const currentNode = nodes[i];
        const nextNode = i < nodes.length - 1 ? nodes[i + 1] : null;
        currentNode.next = nextNode;
    }
    
    return nodes[0];    
};
