class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dynamicMatrix = [0]*n
        dynamicMatrix[0] = 1
        
        for i in range(m):
            for j in range(n):
                dynamicMatrix[j] = 0 if obstacleGrid[i][j] else dynamicMatrix[j] + (0 if j == 0 else dynamicMatrix[j-1])
        return dynamicMatrix[-1]
