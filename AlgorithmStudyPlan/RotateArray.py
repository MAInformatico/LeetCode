class Solution:
    def rotate(self, nums: List[int], k: int) -> None:   
        size = len(nums)
        k = k % size
        nums[:] = nums[size - k:] + nums[:size - k]
