class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        triangle = [[1] * i for i in range(1, numRows+1)]        
        
        if numRows > 2:
          
            for i in range(2, numRows):
                for j in range(len(triangle[i])):
                    if j == 0 or j == n-1:
                        continue
                    
                    triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
        
        return triangle
