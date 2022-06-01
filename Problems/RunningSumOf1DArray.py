class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result, localSum = [], 0
        
        for i in nums:
            localSum += i
            result.append(localSum)
        
        return result
