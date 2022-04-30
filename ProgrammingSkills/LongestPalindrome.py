from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequencies = Counter(s)
        result = 0
        lenS = len(s)
        for i in frequencies:
            result += frequencies[i]//2
        return result*2 + 1 if lenS != 2*result else 2*result
