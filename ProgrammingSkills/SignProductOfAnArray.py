class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result=1
        for n in nums:
            result*=n
        return 1 if result > 1 else (-1 if result < 0 else 0)
