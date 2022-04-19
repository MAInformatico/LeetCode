class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        dictionary1 = {str(i-96): str(chr(i)) for i in range(97, 106)}
        dictionary2 = {str(i-96): str(chr(i)) for i in range(106, 123)}

        result, i = '', 0
		
        while(i < len(s)):            
            if((i+2) < len(s) and s[i+2] == '#'):
                result += dictionary2[str(s[i:i+2])]
                i += 3                
            elif dictionary1[str(s[i])]:
                result += dictionary1[str(s[i])]
                i += 1
                if i == len(s):
                    break
                    
        return result
