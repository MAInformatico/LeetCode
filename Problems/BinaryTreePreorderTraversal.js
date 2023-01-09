/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {    
    let result = [];
    auxFunction(root,result);
    return result;   
};

var auxFunction = function(root, result){
    if(!root) return;
    result.push(root.val);
    auxFunction(root.left,result);
    auxFunction(root.right,result);
}
