class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxLocal = minLocal = result = nums[0]        
        for i in range(1,len(nums)):
            aux = maxLocal
            maxLocal = max(nums[i]*aux,nums[i]*minLocal,nums[i])
            minLocal = min(nums[i]*aux,nums[i]*minLocal,nums[i])
            result = max(result,maxLocal)
        return result
