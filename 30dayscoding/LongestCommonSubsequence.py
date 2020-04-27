class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) 
        n = len(text2) 

        result = [[None]*(n+1) for i in range(m+1)] 

        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    result[i][j] = 0
                elif text1[i-1] == text2[j-1]: 
                    result[i][j] = result[i-1][j-1]+1
                else: 
                    result[i][j] = max(result[i-1][j] , result[i][j-1]) 

        return result[m][n] 
