from collections import deque, Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def DFS(row, column, i):
            if i == len(word):
                return True
            matrix, board[row][column] = board[row][column], '#'
            checked = False
            for coordY, coordX in ((1,0), (-1,0), (0,1), (0,-1)):
                lr, lc = row + coordY, column + coordX
                if 0 <= lr < m and 0 <= lc < n and board[lr][lc] == word[i] and DFS(lr, lc, i+1):
                    checked = True
                    break
            board[row][column] = matrix
            return checked
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and DFS(i, j, 1):
                    return True
        return False
