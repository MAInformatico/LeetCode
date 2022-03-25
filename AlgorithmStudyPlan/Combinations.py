class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n+1)]
        
        else:
            previousValues = self.combine(n,k-1)
            newValues = []
            for i in previousValues:
                for j in range(i[-1] + 1, n + 1):
                    newValues.append(i + [j])
            return newValues
