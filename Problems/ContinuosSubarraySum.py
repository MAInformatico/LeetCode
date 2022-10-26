class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dictionary = {0:-1}
        length = len(nums)
        prefix = 0
        for i in range(length):
            prefix = (prefix + nums[i])%k
            if prefix not in dictionary:
                dictionary[prefix] = i
            else:
                if (i - dictionary[prefix]) >= 2:
                    return True
        return False
