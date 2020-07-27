class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lString = s.split()
        if not lString:
            return 0
        return len(lString[-1])
