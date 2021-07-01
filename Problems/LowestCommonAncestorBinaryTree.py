class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.finder(root, p, q)

    def finder(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node

        leftChild = self.finder(node.left, p, q)
        rightChild = self.finder(node.right, p, q)

        if leftChild and rightChild:
            return node
        else:
            return leftChild or rightChild
