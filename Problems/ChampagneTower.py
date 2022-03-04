class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        matrix = [ [0] * row for row in range(1,100 + 2) ]        
        matrix[0][0] = poured
        
        for i in range(query_row + 1):
            for j in range(i + 1):             
                
                excess = (matrix[i][j] - 1) / 2                
                if excess > 0:
                    matrix[i+1][j] += excess
                    matrix[i+1][j+1] += excess
                
        return min(1, matrix[query_row][query_glass])
