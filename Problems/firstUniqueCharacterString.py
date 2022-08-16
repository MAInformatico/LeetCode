class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = Counter(s)
        for i, value in enumerate(s):
            if result[value] == 1:
                return i
        return -1    
