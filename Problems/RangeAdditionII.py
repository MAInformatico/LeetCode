class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        
        for row, col in ops:
            min_row = min(min_row, row)
            min_col = min(min_col, col)
            
        return min_row * min_col
