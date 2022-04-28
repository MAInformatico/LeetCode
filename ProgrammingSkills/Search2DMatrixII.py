class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        aux = []
        for i in matrix:
            aux += i
        if target in aux:
            return True
        return False
