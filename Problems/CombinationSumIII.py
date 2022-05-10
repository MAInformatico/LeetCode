from itertools import permutations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.backtrack(k,1,n,[])
        return self.result
        
    def backtrack(self,k,start,n,aux):
        if k == 0:
            if n == 0:
                self.result.append(aux.copy())
                return            
        for i in range(start,10):
            aux.append(i)
            self.backtrack(k-1, i+1, n-i, aux)
            aux.pop()
