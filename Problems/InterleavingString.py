class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            else:
                if i == len(s1) and j == len(s2) and (i+j) == len(s3):
                    dp[(i,j)] = True
                    return True
                
                if i < len(s1) and (i+j) < len(s3) and s1[i] == s3[i+j]:
                    if dfs(i+1,j):
                        dp[(i,j)] = True
                        return True 
                    
                if j < len(s2) and (i+j) < len(s3) and s2[j] == s3[i+j] and dfs(i,j+1):
                    dp[(i,j)] = True
                    return True 
                dp[(i,j)] = False
        return dfs(0,0)
