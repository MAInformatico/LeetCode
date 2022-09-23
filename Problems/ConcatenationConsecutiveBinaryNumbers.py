class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        position = 0
        module = 1000000007
        
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                position += 1
                result = ((result << position) + i) % module
        return result
