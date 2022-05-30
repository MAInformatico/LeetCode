class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        signAge = (dividend < 0) ^ (divisor < 0)
        result = len(range(0, abs(dividend)+1, abs(divisor)))-1
        if signAge:
            result = -result
        return min(max(-2147483648, result), 2147483647)
