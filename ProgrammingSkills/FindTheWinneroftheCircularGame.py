class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        @cache
        def dp(n):
            if n == 1:
                return 0
            removeIndex = (k-1) % n
            subIndex = (dp(n-1) + removeIndex) % (n-1)
            return subIndex+1 if subIndex >= removeIndex else subIndex
        return dp(n)+1
