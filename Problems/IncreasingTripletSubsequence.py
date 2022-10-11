class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x = y = float("inf")
        for iterator in nums:
            x = min(x,iterator)
            if iterator > y:
                return True
            elif iterator > x:
                y = iterator
            
        return False
