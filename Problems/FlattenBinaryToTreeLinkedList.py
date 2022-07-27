def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        if not node:
                return node
        right = node.right
        node.right, node.left = node.left, None
        self.flatten(node.right)
        while node.right:
            node = node.right
        node.right = right
        self.flatten(right)
