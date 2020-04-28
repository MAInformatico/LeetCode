class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        for i in A:
            if i == 0:
                result.append(i)
            elif i < 0:
                i *= -1
                i *= i
                result.append(i)
            else:
                i *= i
                result.append(i)

        result.sort()
        return result
