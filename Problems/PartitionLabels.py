class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        dictionary = {}
        
        for i in range(len(s)):
            dictionary[s[i]] = i
            
        currentMax = dictionary[s[0]]
        previousMax = -1
        result = []
        
        for i in range(len(s)):
            
            if(dictionary[s[i]]>currentMax):
                currentMax = dictionary[s[i]]
                
            if(i == currentMax):
                result.append(currentMax - previousMax)
                previousMax = currentMax
                
        return result
