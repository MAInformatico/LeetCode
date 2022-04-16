class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        
        for i in range(len(arr)):
            localSum = 0
            count = 0
            for j in range(i,len(arr)):
                localSum += arr[j]
                if ((count+1)%2 != 0):
                    result += localSum
                count += 1
        
        return result
