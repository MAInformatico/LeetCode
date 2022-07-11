class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def checkerTree(node, depth):
            if not node:
                return
            if depth == len(result):
                result.append(node.val)
            checkerTree(node.right, depth + 1)
            checkerTree(node.left, depth + 1)
            
        checkerTree(root,0)
        return result
