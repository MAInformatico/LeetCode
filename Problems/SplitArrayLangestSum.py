class Solution:
    def splitArray(self, nums: List[int], m: int) -> int: #dynamic programming approach
        
        if not nums or m < 1:
            return None
        if m == 1:
            return sum(nums)
        
        n = len(nums)
        matrix = [[0 for i in range(m)] for j in range(n)]
        
        matrix[0][0] = nums[0]
        for i in range(1,n):
            matrix[i][0] = matrix[i-1][0] + nums[i]
        
        for i in range(1,n):
            for j in range(1,m):
                if j >  i:
                    break
                aux = float('inf')
                accumulate = 0
                for k in range(i-1, -1, -1):
                    accumulate += nums[k+1]
                    localMax = max(matrix[k][j-1], accumulate)
                    aux = min(aux,localMax)
                matrix[i][j] = aux
        
        return matrix[n-1][m-1]
