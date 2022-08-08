class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1 for _ in range(len(nums))]
        for i in range(len(result)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    result[i] = max(result[j] + 1, result[i])
                else:
                    continue
        return max(result)
