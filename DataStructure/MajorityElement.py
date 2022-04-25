class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        reps = collections.Counter(nums)
        return max(reps, key=reps.get)
