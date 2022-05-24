import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        firstColumn = [matrix[i][0] for i in range(len(matrix))]

        row = bisect.bisect(firstColumn, target) - 1
        if matrix[row][0] == target:
            return True

        column = bisect.bisect(matrix[row], target) - 1
        if matrix[row][column] == target:
            return True

        return False
