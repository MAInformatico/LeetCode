class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0        
        nums_set = set(nums)
        longestSecuence = 0
        for i in nums:
            if i-1 not in nums_set:
                length = 0
                while i in nums_set:
                    length += 1
                    i += 1
                longestSecuence = max(longestSecuence, length)
        return longestSecuence
