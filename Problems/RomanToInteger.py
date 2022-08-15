class Solution:
    def romanToInt(self, s: str) -> int:
        dictionaryNums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = 0
        for i in range(len(s)):
            value = dictionaryNums[s[i]]
            if i + 1 < len(s) and dictionaryNums[s[i+1]] > value:
                result -= value
            else:
                result +=value
        return result
