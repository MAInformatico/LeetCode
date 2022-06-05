class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        column = set()
        positiveDiagonal = set()
        negativeDiagonal = set()
        
        def dfs(q):
            nonlocal result
            if q == n:
                result += 1
                return
            for i in range(n):
                if i in column or q+i in positiveDiagonal or q-i in negativeDiagonal:
                    continue
                column.add(i)
                positiveDiagonal.add(q+i)
                negativeDiagonal.add(q-i)
                dfs(q+1)
                column.remove(i)
                positiveDiagonal.remove(q+i)
                negativeDiagonal.remove(q-i)
        dfs(0)                
        return result  
