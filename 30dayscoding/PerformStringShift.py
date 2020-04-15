class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        result = 0
        for i, j in shift:
            if i == 0:
                result += j
            else:
                result -= j
        
        result %= len(s)
        return s[result:] + s[:result]
