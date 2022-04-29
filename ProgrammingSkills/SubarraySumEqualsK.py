class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        suma = 0
        dictionary = {0:1}
        
        for i in nums:
            suma += i
            
            if suma -k in dictionary:
                    result += dictionary[suma-k]
                    
            if suma not in dictionary:
                dictionary[suma] = 1
            else:
                dictionary[suma] += 1
                        
        return result
