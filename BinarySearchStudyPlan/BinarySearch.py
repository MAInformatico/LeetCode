class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, target, 0, len(nums)-1)
    
    def find(self,nums,target,begin,end):
        if begin > end:
            return -1
        middle = begin + (end - begin) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            return self.find(nums, target, begin, middle -1)
        else:
            return self.find(nums, target, middle + 1 ,end)
