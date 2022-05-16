class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        path = deque([(1,(0,0))])
        m, n = len(grid), len(grid[0])
        visited =set()
        
        while path:
            d, (i, j) = path.popleft()
            if grid[i][j] == 1: continue
            if (i,j) in visited: continue
            if (i,j) == (m-1,n-1):
                return d
            
            visited.add((i,j))
            
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[1,-1],[-1,-1]]:
                if 0<=i+di<len(grid) and 0<=j+dj<len(grid[0]):
                    path.append((d+1,(i+di,j+dj)))
        return -1
