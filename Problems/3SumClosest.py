class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums = sorted(nums)
        for i in range(len(nums)-1):
            left, right = i+1, len(nums)-1
            while (left < right):
                aux = nums[i]+nums[left]+nums[right]                
                if aux==target:
                    return target
                elif abs(aux-target) < diff:
                    diff=abs(target-aux)
                    result = aux
                if aux > target:
                    right -= 1
                else:
                    left += 1
        return result
