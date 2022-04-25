class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        reps = collections.Counter(nums)
        return min(reps, key=reps.get)
