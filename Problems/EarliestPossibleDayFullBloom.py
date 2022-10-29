class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        result = 0
        for i,j in sorted(zip(growTime,plantTime)):
            result = i + j if i >= result else result + j
        
        return result
