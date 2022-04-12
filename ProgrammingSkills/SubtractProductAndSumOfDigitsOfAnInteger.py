class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        aux = [int(i) for i in str(n)]
        sumAux = 0
        multiply = 1
        for i in range(len(aux)):
            sumAux += int(aux[i])
            multiply *= int(aux[i])
        
        return multiply - sumAux
