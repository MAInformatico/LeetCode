class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        lenMatrix = len(matrix)
        lenColumn = len(matrix[0])
        
        for i in range(1,lenMatrix):
            for j in range(1, lenColumn):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        
        return True
