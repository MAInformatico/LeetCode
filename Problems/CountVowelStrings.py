class Solution:
    def countVowelStrings(self, n: int) -> int:
        matrix = [[0]*6 for _ in range(n+1)] #dynamic programming approach
        for i in range(1,6):
            matrix[1][i] = i
            
        for i in range(2, n+1):
            matrix[i][1] = 1
            for j in range(2,6):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        
        return matrix[n][5]
