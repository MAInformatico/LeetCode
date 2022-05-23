class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = aux = 0
        for i in range(len(grid)):

            aux = next(filter(lambda x:x<0, grid[i]),grid[i][0])
            if aux < 0:
                result += len(grid[i][grid[i].index(aux):])
                
        return result
