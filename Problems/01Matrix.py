class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:               
        row, col = len(mat), len(mat[0])
        result = [[-1]*col for _ in range(row)]
        dQueue = collections.deque([])

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    dQueue.append((i, j, 0))

        while dQueue:
            i, j, distance = dQueue.popleft()
            if i<0 or i>=row: continue
            if j<0 or j>=col: continue
            if result[i][j]!=-1: continue
            result[i][j] = distance

            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                dQueue.append((ni, nj, distance+1))

        return result
