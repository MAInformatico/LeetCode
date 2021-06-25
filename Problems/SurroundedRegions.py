class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return board
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        board[i][j] = 'V'
                        aux = [(i,j)]
                        while aux:
                            x,y = aux.pop(0)
                            if x+1 < m and board[x+1][y] == 'O':
                                board[x+1][y] = 'V'
                                aux.append((x+1,y))
                            if y+1 < n and board[x][y+1] == 'O':
                                board[x][y+1] = 'V'
                                aux.append((x,y+1)) 
                            if x-1 >= 0 and board[x-1][y] == 'O':
                                board[x-1][y] = 'V'
                                aux.append((x-1,y))
                            if y-1 >= 0 and board[x][y-1] == 'O':
                                board[x][y-1] = 'V'
                                aux.append((x,y-1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else: board[i][j] = 'X'
