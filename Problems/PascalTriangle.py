class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]        
        for row in range(numRows-1):
            auxMatrix = [1]
            for column in range(1, row+1):
                auxMatrix.append(result[row][column-1] + result[row][column])                
            auxMatrix.append(1)
            result.append(auxMatrix)            
        return result
