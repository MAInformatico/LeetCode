# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result, level = [], [root]
        while level and level[0]:
            result= [[node.val for node in level]] + result         
            level = [kidNode for n in level for kidNode in (n.left, n.right) if kidNode]
        return result
