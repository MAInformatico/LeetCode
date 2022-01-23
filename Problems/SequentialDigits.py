class Solution:
    
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []        
        
        def dfs(num): #Dynamic programming time!            
            if num >= low and num <= high:
                result.append(num)
            
            if num > high:
                return
            
            y = num % 10
            
            if y != 9:
                dfs(num*10 + (y + 1))
                
        for i in range(1,10):
            dfs(i)        
        return sorted(result)
