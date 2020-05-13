class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        sortedArray = sorted(heights)
        for i in range(0, len(heights)):
            if heights[i] != sortedArray[i]:
                result += 1
        return result
