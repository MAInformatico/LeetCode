class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        minimumPrice = [float("inf")] * (k + 1)
        maximumProfit = [0] * (k + 1)
        
        for i in prices:
            for j in range(1, k + 1):
                minimumPrice[j] = min(minimumPrice[j], i - maximumProfit[j - 1])
                maximumProfit[j] = max(maximumProfit[j], i - minimumPrice[j])
                
        return maximumProfit[k]
