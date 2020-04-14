class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total_sum = 0
        index_map = dict()
        index_map[0] = -1
        result = 0        
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1
            if total_sum in index_map:
                result = max(result, i - index_map[total_sum])
            else:
                index_map[total_sum] = i
        return result
