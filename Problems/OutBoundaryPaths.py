class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def solve(i, j, maxMove):
            if maxMove < 0: #There are not more possible movements allowed
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            x = solve(i-1, j, maxMove - 1) #movement positive x axis
            nx = solve(i+1, j, maxMove - 1) #movement negative x axis
            ny = solve(i, j-1, maxMove - 1) #movement negative y axis
            y = solve(i, j+1, maxMove - 1) #movement positive y axis
            
            return x + nx + ny + y
        
        return solve(startRow, startColumn, maxMove) % 1000000007
