class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            result.append(pow(i,2))
        
        return sorted(result, reverse = False)
