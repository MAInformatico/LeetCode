# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0        
        else:
            count = 0
            result = []
            queue = deque()
            queue.append(root)

            while queue:
                level = []
                for _ in range(len(queue)):
                    current = queue.popleft()
                    level.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                result.append(level)
                count += 1

            return count
