class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []   
        for i in range(len(s)):
            if s[i] in result:
                continue  
            while result and s[i]<result[-1] and result[-1] in s[i+1:]:   
                result.pop()                 
            result.append(s[i])       
        
        return "".join(result)      
