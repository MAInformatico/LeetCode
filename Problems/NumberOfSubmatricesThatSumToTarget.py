from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for i in range(1,len(row)):
                row[i] += row[i-1]
        result = 0
        for i in range(len(matrix)):
            aux = [0 for val in matrix[i]]
            for j in range(i,len(matrix)):
                need = defaultdict(int)
                need[target] = 1
                for k in range(len(matrix[0])):
                    aux[k] += matrix[j][k]
                    if aux[k] in need:
                        result += need[aux[k]]
                    need[aux[k]+target] += 1
        return result
