class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: #empty list
            return -1
        if len(nums) == 1:
            if nums[0] == target: return 0
            else: return -1
        if len(nums) == 2:
            if nums[0] == target: return 0
            elif nums[1] == target: return 1
            else: return -1

        m = (0+len(nums))//2
        if (nums[m]-nums[0])*(nums[m]-nums[-1]) < 0:
            l0, r0 = 0, len(nums)
            while l0 < r0: 
                m0 = (l0+r0)//2
                if nums[m0] < target:
                    l0 = m0+1
                else:
                    r0 = m0
            if (l0 < len(nums)) and (nums[l0] == target): return l0
            else: return -1
                
        l, r = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        if (nums[l]-target)*(target-nums[l+1]) < 0: return -1
        
        if target <= nums[-1]:
            l1, r1 = l+1, len(nums)
        else:
            l1, r1 = 0, l       
        while l1 < r1: 
            m1 = (l1+r1)//2
            if nums[m1] < target:
                l1 = m1+1
            else:
                r1 = m1
        if nums[l1] == target: return l1
        else: return -1
