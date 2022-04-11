class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        rotated = []
        
        for i in grid:
            rotated += i
        
        rotated = rotated[-k:] + rotated[:-k]
                
        return [rotated[i * n: (i + 1) * n] for i in range(m)]       
