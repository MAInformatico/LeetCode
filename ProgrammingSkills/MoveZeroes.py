class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        while length >= 0:
            if nums[length] == 0:
                nums.append(nums.pop(length))
            length -= 1
