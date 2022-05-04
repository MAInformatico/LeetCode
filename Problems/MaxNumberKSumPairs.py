class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        left = 0
        right = len(nums) - 1
        
        while left < right:
            current = nums[left] + nums[right]
            if current == k:
                result += 1
                left += 1
                right -= 1
            elif current < k:
                left += 1
            else:
                right -= 1
            
        return result
