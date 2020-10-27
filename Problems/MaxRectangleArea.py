class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        TDAstack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[TDAstack[-1]]:
                height = heights[TDAstack.pop()]
                width = i - TDAstack[-1] - 1
                result = max(result, height * width)
            TDAstack.append(i)
        heights.pop()
        return result
