/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
  if(n ===0) return []
    function generate(start,end) {
        let result = []
        if(end===start) {
            return [new TreeNode(start)]
        }
        if(end<start) {
            return [null]
        }
        for(let i=start;i<=end;i++) {
            const left = generate(start,i-1)
            const right = generate(i+1,end)
            for(let k = 0;k<left.length;k++) {
                for(let j = 0;j<right.length;j++) {
                    const node = new TreeNode(i)
                    node.left = left[k]
                    node.right = right[j]
                    result.push(node)
                }
            }
        }
        return result
    }
    return generate(1,n)  
};
