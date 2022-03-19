class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring = []
        result = 0
        
        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                result = max(result,len(substring))
                substring = substring[substring.index(s[i])+1:]
                substring.append(s[i])
        
        result = max(result,len(substring))
        return result 
