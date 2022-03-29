class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            aux = target - nums[i]
            if aux in nums and nums.index(aux) != i:
                result.append(i)
                result.append(nums.index(aux))
                return result
