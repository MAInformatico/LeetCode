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
 * @return {boolean}
 */
var isSymmetric = function(root) {    
    if(!root) return true;
    return dfs(root.left, root.right);        
};

function dfs(branchLeft, branchRight){
  if(!branchLeft && !branchRight) return true;
  if((!branchLeft || !branchRight) || (branchLeft.val !== branchRight.val)) return false;
  
  return dfs(branchLeft.left, branchRight.right) && dfs(branchLeft.right, branchRight.left);
}
