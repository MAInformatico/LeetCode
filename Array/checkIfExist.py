class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashTable = set()
        for i in range(len(arr)):
            n = arr[i]
            if 2*n in hashTable or n/2 in hashTable:
                return True
            hashTable.add(n)
            
        return False
