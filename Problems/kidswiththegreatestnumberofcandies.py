class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        currentMax = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] >= currentMax:
                result.append(True)
            else:
                result.append(False)
        return result
