# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, current_path, aux):
        if not root:
            return []
        
        if not root.left and not root.right and current_path - root.val == 0:
            self.val.append(aux + [root.val])
        
        left_branch = self.dfs(root.left, current_path - root.val, aux + [root.val])
        right_branch = self.dfs(root.right, current_path - root.val, aux + [root.val])
        return left_branch and right_branch
    
    def pathSum(self, root: TreeNode, current_path: int) -> List[List[int]]:
        self.val = []
        self.dfs(root, current_path, [])
        return self.val
