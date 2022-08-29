class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        result = 0
        
        def DFS(i, j, grid, row, column):
            if i<0 or j<0 or i>row-1 or j>column-1 or grid[i][j] != "1": 
                return
            
            grid[i][j] = "*"
            
            DFS(i+1, j, grid, row, column)
            DFS(i-1, j, grid, row, column)
            DFS(i, j+1, grid, row, column)
            DFS(i, j-1, grid, row, column)
            
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1":
                    DFS(i, j, grid, row, column)
                    result += 1
        
        return result
