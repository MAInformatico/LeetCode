from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dnums = defaultdict(int)
        currentsum = 0
        result = 0
        for v in nums:
            currentsum += v
            if currentsum == k:
                result += 1
            if (currentsum - k) in dnums:
                result += dnums[currentsum - k]
            dnums[currentsum] += 1
        return result
