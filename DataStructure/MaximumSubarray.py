class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        aux = nums
        
        for i in range(1, len(nums)):
            aux[i] = max(aux[i], aux[i-1] + nums[i])
                
        return max(aux)
