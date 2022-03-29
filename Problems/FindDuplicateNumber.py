class Solution:
    def findDuplicate(self, nums: List[int]) -> int:        
        withoutDuplicates = set(nums)
        return (sum(nums)-sum(withoutDuplicates))//(len(nums)-len(withoutDuplicates))
