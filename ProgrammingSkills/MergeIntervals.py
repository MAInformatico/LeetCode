class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        minimalValueInterval = sorted([i[0] for i in intervals])        
        maximalValueInterval = sorted([i[1] for i in intervals])
        result = []
        aux = minimalValueInterval[0]
        i = 0
        while i<(len(minimalValueInterval)-1):
            if maximalValueInterval[i]>=minimalValueInterval[i+1]:
                i+=1
                continue
            result.append([aux,maximalValueInterval[i]])
            aux = minimalValueInterval[i+1]
            i+=1
        result.append([aux,maximalValueInterval[-1]])
        return result
