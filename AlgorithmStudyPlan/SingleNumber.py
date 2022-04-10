from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        aux = Counter(nums).most_common(len(nums))
        aux = list(aux[-1])
        return aux[-2] 
