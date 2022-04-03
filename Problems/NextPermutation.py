class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        j = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                j = i
        if j == -1:
            nums[:] = nums[::-1]
            return
        
        for i in range(j + 1, len(nums)):
            if nums[i] > nums[j]:
                k = i

        nums[j], nums[k] = nums[k], nums[j]
        
        nums[j+1:] = nums[:j:-1]
