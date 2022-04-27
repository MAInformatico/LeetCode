class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        number = 1
        
        result = [ [0]*n for i in range(n)]
        
        left,right,top,bottom = 0, n-1, 0, n-1
        
        while left <= right and top <= bottom:
            
            for i in range(left,right+1):
                result[top][i] = number
                number += 1
            top += 1
            
            for i in range(top,bottom+1):
                result[i][right] = number
                number += 1
            right -= 1
            
            for i in range(right, left-1,-1):
                result[bottom][i] = number
                number += 1
            bottom -= 1
            
            for i in range(bottom,top-1,-1):
                result[i][left] = number
                number += 1
            left += 1
        
        return result
