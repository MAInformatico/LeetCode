class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1:
            return False
        
        numberString = str(n)
        aux = []
        
        while True:
            if int(numberString) == 1:
                return True
            elif (len(numberString) == 1) and (int(numberString) != 7):
                return False

            for i in range(len(numberString)):
                aux.append(int(numberString[i]))
                aux[i] = aux[i] **2
            
            numberString = str(sum(aux))
            aux = []
