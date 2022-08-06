class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        result = log2(buckets)
        minutesToTest = ceil(minutesToTest/minutesToDie)

        if minutesToTest == 1: return ceil(result)
        return ceil(result / log2(minutesToTest+1))
