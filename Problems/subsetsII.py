class Solution:    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        nums.sort()
        result = [[]]
        previous_size = 0
        for i in range(len(nums)):
            size = len(result)
            for j in range(size):
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    result.append(list(result[j]))
                    result[-1].append(nums[i])
            previous_size = size
        return result
