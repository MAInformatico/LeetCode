class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        maximum = max(nums,key=lambda x:len(x))
        maxLen = len(maximum)
        nums = sorted(nums, key = lambda x:str(x * (10*(maxLen-len(x) + 1))),reverse = True)       
        result = "".join(nums)
        result = int(result)//1
        return str(result)
