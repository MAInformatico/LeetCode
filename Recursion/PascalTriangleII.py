class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = [1 for i in range(rowIndex+1)]
        
        for row in range(2, rowIndex + 1):
            for col in range(row-1, 0, -1):
                result[col] = result[col] + result[col-1]

        return result
