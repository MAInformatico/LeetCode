class Solution:
    def hammingWeight(self, n: int) -> int:
        currentValue = n
        counterOnes = 0
        while currentValue > 0:
            currentValue, remainder = divmod(currentValue, 2)
            counterOnes += remainder

        return counterOnes
