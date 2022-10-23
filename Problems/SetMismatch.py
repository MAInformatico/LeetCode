class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, x, y = len(nums), sum(nums), sum(set(nums))
        
        s = n*(n+1)//2
        
        return [x-y, s-y]
