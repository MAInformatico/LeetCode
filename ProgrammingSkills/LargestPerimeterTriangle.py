class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:        
        nums.sort()
        length = len(nums)
        a, b, c = length - 1, length - 2, length - 3
        
        while c != -1: #validate
            if nums[a] < (nums[b] + nums[c]):
                return nums[a] + (nums[b] + nums[c])
            else:
                a -= 1
                b -= 1
                c -= 1
        return 0
