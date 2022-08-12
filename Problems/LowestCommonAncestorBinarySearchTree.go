/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {	
    var current *TreeNode = root
    for current != nil {
        if p.Val < current.Val && q.Val < current.Val {
            current = current.Left
        } else if p.Val > current.Val && q.Val > current.Val {
            current = current.Right
        } else {
            break
        }
    }
    return current    
}
