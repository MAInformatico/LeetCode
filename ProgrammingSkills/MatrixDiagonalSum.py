class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            result += mat[i][i] + mat[i][~i]
        if (len(mat) % 2):
            result -= mat[int(i/2)][int(i/2)]
            
        return result
