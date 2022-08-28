class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dictDiagonal = {}
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                dictDiagonal.setdefault(j-i, [])
                dictDiagonal[j-i].append(mat[i][j])
        
        for key, value in dictDiagonal.items():
            dictDiagonal[key] = sorted(value)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = dictDiagonal[j-i].pop(0)
        
        return mat
