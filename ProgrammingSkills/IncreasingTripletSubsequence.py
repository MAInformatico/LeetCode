class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        k = 3
        result = []
        for i in nums:
            x = bisect.bisect_left(result,i)
            if x == len(result):
                result.append(i)
            else:
                result[x] = i
            
            if len(result) == k:
                return True
            
        return False
