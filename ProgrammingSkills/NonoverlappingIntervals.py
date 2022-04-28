class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        previousEnd = intervals[0][1]
        result = 0
        
        for i, j in intervals[1:]:
            if i >= previousEnd:
                previousEnd = j
            else:
                result += 1
                previousEnd = min(previousEnd, j)
        return result
