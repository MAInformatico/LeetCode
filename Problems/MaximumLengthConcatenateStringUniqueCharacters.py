class Solution:
    def maxLength(self, arr: List[str]) -> int:
        matrix = [set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in matrix[:]:
                if i & j:
                    continue
                
                matrix.append(i|j)
        return max(len(i) for i in matrix)
