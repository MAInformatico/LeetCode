class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        if n == 1:
            result.append(0)
        
        def DFS(num, visited):
            if visited == 0:
                result.append(num)
                return
            
            lastDigit = num % 10
            
            if lastDigit >= k:
                DFS(num*10 + lastDigit - k, visited - 1)
            
            if k > 0 and lastDigit + k < 10:
                DFS(num*10 + lastDigit + k, visited - 1)
                
        for i in range(1,10):
            DFS(i, n - 1)
            
        return result
