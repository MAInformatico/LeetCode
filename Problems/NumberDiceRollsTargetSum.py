class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        module = 10**9 + 7
        matrix = [[0 for _ in range(target+1)] for _ in range(n+1)]
        matrix[0][0] = 1
        previous = 0
        
        for i in range(1, n+1):            
            previous = 0
            for j in range(i, min(k+1, target+1)):
                previous = (previous + matrix[i-1][j-1]) % module
                matrix[i][j] = previous
                
            for l in range(k+1, target+1):
                previous = (previous + matrix[i-1][l-1] - matrix[i-1][l-k-1]) % module
                matrix[i][l] = previous
                
        return matrix[n][target]
