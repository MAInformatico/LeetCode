class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int((c/2) ** 0.5) + 1):
            b = (c - i ** 2) ** 0.5
            if b.is_integer():
                return True
        return False
