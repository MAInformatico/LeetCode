class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        currentColor = image[sr][sc]
        
        def dfs(i, j):
            if (i == m or j == n or i < 0 or j < 0 or image[i][j] != currentColor):
                return
            
            image[i][j] = newColor
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        if image[sr][sc] == newColor:
            return image
        
        dfs(sr, sc)
        return image
