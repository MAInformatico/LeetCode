class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenMatrix = len(matrix)
        for i in range(lenMatrix):
            for j in range(i,lenMatrix):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
