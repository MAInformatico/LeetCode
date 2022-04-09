class Solution:
    def hammingWeight(self, n: int) -> int:
        aux = str(bin(n))
        result = 0
        
        for i in aux:
            if i == '1':
                result += 1
        
        return result
