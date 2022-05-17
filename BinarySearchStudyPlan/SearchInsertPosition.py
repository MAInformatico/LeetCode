class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, i in enumerate(nums):
                if i >= target:
                    return index
            
        return len(nums)
