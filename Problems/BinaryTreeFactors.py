class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        
        dynamicProgramming = {i:1 for i in arr}
        
        for i in range(len(arr)):
            for j in range(i):
                if arr[i]%arr[j] == 0 and arr[i]//arr[j] in dynamicProgramming:
                    left = arr[j]
                    right = arr[i]//arr[j]
                    
                    dynamicProgramming[arr[i]] = dynamicProgramming[arr[i]] + dynamicProgramming[left] * dynamicProgramming[right]
                    
        return sum([dynamicProgramming[i] for i in arr]) % (10**9 + 7)
