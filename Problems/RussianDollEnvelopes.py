class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        dynamicMatrix, maxEnv = [1] * len(envelopes), 1
        
        for i in range(1, len(envelopes)):
            for j in range(0,i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dynamicMatrix[i] = max(dynamicMatrix[i], 1 + dynamicMatrix[j])
                    maxEnv = max(maxEnv, dynamicMatrix[i])
        
        return maxEnv
