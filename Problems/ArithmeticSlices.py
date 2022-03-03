class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        else:
            count,result = 0,0
            for i in range(1,len(nums)-1):
                if nums[i+1]-nums[i] == nums[i]-nums[i-1]:
                    count += 1
                else:
                    count = 0
                result += count              
            return result
