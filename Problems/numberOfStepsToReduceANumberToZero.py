class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0:
            if num&1:
                num -= 1
            else:
                num //= 2
            result += 1
        return result
