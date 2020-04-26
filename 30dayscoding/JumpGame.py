class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = len(nums)-1
        for i in range(len(nums)-2,-1,-1): 
            if (i + nums[i]) >= result: 
                result = i 
        return result == 0
