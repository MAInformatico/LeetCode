
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = dict()
        result = []
        
        for i in nums:
            dictionary[i] = dictionary.get(i,0) + 1
            
        for i in range(k):
            findMax = max(dictionary, key=dictionary.get)
            result.append(findMax)
            del dictionary[findMax]
            
        return result
