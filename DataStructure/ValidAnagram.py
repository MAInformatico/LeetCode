from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s) != len(t):
            return False

        countS = dict(Counter(s))
        countT = dict(Counter(t))

        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True
