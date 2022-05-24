class Solution:
    def mySqrt(self, x: int) -> int:
        result, i = 0, 1
        while x > 0:
            result += 1
            x -= i
            i += 2
        if x == 0:
            return result
        
        return result - 1
