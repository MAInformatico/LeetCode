class Solution:
    def trailingZeroes(self, n: int) -> int:        
        countZeros = 0
        while(n >= 5):
            n //= 5
            countZeros += n
        
        return countZeros
