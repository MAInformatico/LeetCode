class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        newArray = []
        for i in range(len(A)):
            if A[i]%2 == 0:
                newArray.append(A[i])
        for i in range(len(A)):
            if A[i]%2 != 0:
                newArray.append(A[i])
        
        return newArray
