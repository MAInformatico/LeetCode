class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=itemgetter(0), reverse=True)
        
        currentAttack = properties[0][0]
        previousBestDefense = 0
        currentBestDefense = 0
        
        result = 0
        
        for i, j in properties:
            if i != currentAttack:
                previousBestDefense = currentBestDefense
                currentAttack = i
            
            currentBestDefense = max(currentBestDefense, j)
            
            if j < previousBestDefense:
                result += 1
    
        return result
