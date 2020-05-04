class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1 for _ in range(size)]
        left = [1 for _ in range(size)]
        right = [1 for _ in range(size)]
        
        for i in range(1,size):
            left[i] = left[i-1] * nums[i-1]
            
        for i in range(size-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
            
        for i in range(size):
            result[i] = left[i] * right[i]
            
        return result
