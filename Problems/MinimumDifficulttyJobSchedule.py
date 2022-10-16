class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def auxiliar(index, cut):
            if cut == d:
                return max(jobDifficulty[index:])
            current = -1e9
            result = 1e9
            for i in range(index, length-d+cut):
                current = max(current, jobDifficulty[i])
                result = min(result, current+auxiliar(i+1, cut+1))
            return result
        
        length = len(jobDifficulty)
        
        if length < d:
            return -1
        
        return auxiliar(0, 1)
