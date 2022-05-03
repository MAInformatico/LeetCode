class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        aux = set()
        
        i, j = 0, 9
        
        while j < len(s):
          
            if s[i:j+1] in aux:
                if s[i:j+1] not in result:
                    result.append(s[i:j+1])                    
                i += 1
                j += 1
                
            elif s[i:j+1] not in aux:
                aux.add(s[i:j+1])
                i += 1
                j += 1
        
        return result
