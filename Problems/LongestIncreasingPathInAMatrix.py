class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dictionaryMemo={}
        steps=[(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(i,j):
            if (i,j) in dictionaryMemo:
                return dictionaryMemo[(i,j)]
            count = 1
            for x,y in steps:
                a,b = i+x,j+y 
                if a >= 0 and a <= len(matrix)-1 and b >= 0 and b <= len(matrix[0])-1 and matrix[a][b] > matrix[i][j]:
                    count = max(count, 1+dfs(a,b))
            dictionaryMemo[(i,j)] = count
            return count
        
        result = 1 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dfs(i,j))
        return result
