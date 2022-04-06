from collections import defaultdict

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dynamicMatrix = defaultdict(int)
        result = 0
        mod = 10**9+7
        
        for i in range(2, len(arr)):
            for j in range(i-1):                
                dynamicMatrix[arr[j] + arr[i-1]] += 1
                
            result += dynamicMatrix[target - arr[i]]
            result %= mod
            
        return result
