class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        moves = ((-1,0),(1,0),(0,-1),(0,1))
        area = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                area = max(area,dfs(grid,visited,moves,i,j))
        return area
    
def dfs(grid,visited,moves,r,c):
    if (r < 0 or r >= len(grid) or
        c < 0 or c >= len(grid[0]) or
        not grid[r][c] or
        (r,c) in visited):
        
        return 0
    
    area = 1
    visited.add((r,c))
    for move in moves:
        row = r + move[0]
        col = c + move[1]
        area += dfs(grid,visited,moves,row,col)
    return area
