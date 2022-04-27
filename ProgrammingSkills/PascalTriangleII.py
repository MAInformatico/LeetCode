class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        rowIndex += 1
        
        for i in range(1,rowIndex):
            number = result[-1]*(rowIndex-i)
            number = number//i
            result.append(number)
        
        return result
