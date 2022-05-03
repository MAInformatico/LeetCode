class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        aux = nums[:]     
        aux.sort()
        init = 0
        end = len(nums) - 1
        
        while init <= end and (nums[init] == aux[init] or nums[end] == aux[end]):
            if nums[init] == aux[init]:
                init += 1
            if nums[end] == aux[end]:
                end -= 1
                
        return end - init + 1 if end - init > 0 else 0
