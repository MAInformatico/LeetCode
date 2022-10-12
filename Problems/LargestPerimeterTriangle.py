class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result = 0
        if len(nums) < 3:
            return result
        nums.sort(reverse=True)        
        x, y = nums[:2]
        for i in nums[2:]:
            if y + i > x:                
                result = x + y + i
                return result
            x, y = y, i
        return result
