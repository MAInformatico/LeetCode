class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:        
        result = []
        s = 0
        
        for i in nums:
            if i%2 == 0:
                s += i
        
        for i,j in queries:
            if nums[j]%2 == 0:
                s -= nums[j]
            aux = nums[j] + i
            if aux%2 == 0:
                s += aux
            nums[j] = aux
            result.append(s)
            
        return result
