# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        midValues = nums[len(nums)//2]
        result = TreeNode(midValues)
        result.left = self.sortedArrayToBST(nums[:len(nums)//2])
        result.right = self.sortedArrayToBST(nums[len(nums)//2 +1 :])
        return result
