from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lenN = len(nums)
        result = [None]*lenN
        aux = SortedList()
        for i in reversed(range(lenN)):
            result[i] = aux.bisect_left(nums[i])
            aux.add(nums[i])
        return result
