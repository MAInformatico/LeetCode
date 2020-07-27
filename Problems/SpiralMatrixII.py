class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        counter = 1
        while left <= right and top <= bottom:
            #---> right
            for i in range(left, right + 1):
                matrix[top][i] = counter
                counter += 1
            top += 1

            #down
            for i in range(top, bottom + 1):
                matrix[i][right] = counter
                counter += 1
            right -= 1

            #<----- left
            for i in range(right, left-1, -1):
                matrix[bottom][i] = counter
                counter += 1
            bottom -= 1

            #up
            for i in range(bottom, top-1, -1):
                matrix[i][left] = counter
                counter += 1
            left += 1

        return matrix
