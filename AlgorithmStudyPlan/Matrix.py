class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        matrix = [[math.inf] if mat[i][j] != 0 else 0 for j in range(n) for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i > 0:
                    matrix[i][j] = min(matrix[i][j], 1 + matrix[i - 1][j])
                if j > 0:
                    matrix[i][j] = min(matrix[i][j], 1 + matrix[i][j - 1])
                    
        for i in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                if i < m - 1:
                    matrix[i][j] = min(matrix[i][j], 1 + matrix[i + 1][j])
                    matrix[i][j] = min(matrix[i][j], 1 + matrix[i][j+1])
        
        return matrix
    
