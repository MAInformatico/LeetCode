# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([(root,[root.val],root.val)])
        
        while queue:
            node, path, currentSum = queue.popleft()
            
            if not node.left and not node.right:
                if currentSum == targetSum:
                    result.append(path)
                    continue
            
            if node.left:
                queue.append((node.left, path + [node.left.val], currentSum+node.left.val))
            if node.right:
                queue.append((node.right, path + [node.right.val], currentSum+node.right.val))
        
        return result
