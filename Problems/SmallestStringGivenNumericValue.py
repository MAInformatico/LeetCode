class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        x = (k - n) // 25
        smallestStringCharacter = chr(k - x * 25 - n + 97) if n - x else ""
        return "a" * (n - x - 1) + smallestStringCharacter + "z" * x
