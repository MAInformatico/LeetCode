class Solution:
    
    def isValidRow(self, board, row):
        validRow = []
        
        for i in range(len(board)):
            if board[row][i] != '.':
                if board[row][i] in validRow:
                    return False
                else:
                    validRow.append(board[row][i])
        return True
    
    # Check the column
    def isValidCol(self, board, col):
        validCol = []
        
        for i in range(len(board)):
            if board[i][col] != '.':
                if board[i][col] in validCol:
                    return False
                else:
                    validCol.append(board[i][col])
        return True
    
    # Check the 3 x 3 matrix
    def isValidBox(self, board, startRow, startCol):
        validBox = []
        
        for i in range(3):
            for j in range(3):
                if board[i + startRow][j + startCol] != '.':
                    if board[i + startRow][j + startCol] in validBox:
                        return False
                    else:
                        validBox.append(board[i + startRow][j + startCol])
        
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.isValidRow(board, i) or not self.isValidCol(board, i):
                return False
        
        for j in range(0, len(board), 3):
            for k in range(0, len(board), 3):
                if not self.isValidBox(board, j, k):
                    return False
                
        return True
