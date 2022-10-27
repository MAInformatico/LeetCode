class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        MatrixA, MatrixB, result = [], [], collection.defaultdict(int)
        
        for row in range(len(img1)):
            for column in range(len(img1[row])):
                if img1[row][column]:
                    MatrixA.append((row,column))
                if img2[row][column]:
                    MatrixB.append((row,column))
        
        for rowA, columnA in MatrixA:
            for rowB, columnB in MatrixB:
                result[(rowB - rowA, columnB - columnA)] += 1
        
        return max(result.values() or [0])
