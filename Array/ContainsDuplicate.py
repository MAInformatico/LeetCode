class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        dicti = {}
        for i in nums:
            if i not in dicti:
                dicti[i] = True
            else:
                return dicti[i]
        return False
