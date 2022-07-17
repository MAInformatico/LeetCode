class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        maxPossibleInversions = (n * (n-1)//2)
        if k > maxPossibleInversions:
            return 0
        if k == 0 or k == maxPossibleInversions:
            return 1
        
        MOD = pow(10,9) + 7
        
        matrix = [[0]*(k+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            matrix[i][0] = 1

        matrix[2][1] = 1
        
        for i in range(3,n+1):
            maxPossibleInversions = min(k, i*(i-1)//2)
            for j in range(1,  maxPossibleInversions + 1):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] 
                if j>=i:
                    matrix[i][j] -= matrix[i-1][j - i]
                matrix[i][j] = (matrix[i][j] + MOD) % MOD
            
        return matrix[n][k]
