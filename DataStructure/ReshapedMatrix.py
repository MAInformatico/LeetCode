class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        values = []
        for i in mat:
            values += i
        
        if len(values) != r*c:
            return mat
        else:
            reshapedMatrix = []
            for row in range(r):
                matRrow = values[:c]
                values[:] = values[c:]
                reshapedMatrix.append(matRow)
            return reshapedMatrix
