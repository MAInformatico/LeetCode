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
 * @return {TreeNode}
 */
var invertTree = function(root) {    
    const auxStack = [root];
    
    while(auxStack.length){        
        const node = auxStack.pop();
        
        if(node != null){            
            auxStack.push(node.left);
            auxStack.push(node.right);
            
            const temp = node.left;
            node.left = node.right;
            node.right = temp;
        }
    }
    return root;
};
