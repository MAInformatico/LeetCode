class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:        
        if not grid or not grid[0]: return 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    aux = 0
                elif i == 0:
                    aux = grid[i][j-1]
                elif j == 0:
                    aux = grid[i-1][j]
                else:
                    aux = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = aux + grid[i][j]
        return grid[r-1][c-1]
