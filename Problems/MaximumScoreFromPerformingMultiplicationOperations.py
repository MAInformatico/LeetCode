class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:  
        m, n = len(multipliers), len(nums)

        matrix = [[-float("inf")]*(m+1) for _ in range(m+1)]
        
        matrix[0][0] = 0
        for i in range(1, m+1):
            matrix[i][0] = matrix[i-1][0]+multipliers[i-1]*nums[i-1]
            matrix[0][i] = matrix[0][i-1]+multipliers[i-1]*nums[-i]
        
        result = -float("inf")
        for i in range(1, m+1):
            for j in range(i+1):
                nRight = i-j
                matrix[j][nRight] = max(matrix[j-1][nRight]+multipliers[i-1]*nums[j-1],
                                          matrix[j][nRight-1]+multipliers[i-1]*nums[-nRight])
                if i == m:
                    result = max(result, matrix[j][nRight])
                    
        return result
