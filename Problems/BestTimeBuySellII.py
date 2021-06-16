class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minimal = float('inf')
        maxOneTx = 0
        sellOneTx = float('inf')
        maxTwoTx = 0
        for price in prices:
            minimal = min(minimal, price)
            maxOneTx = max(maxOneTx, price-minimal)
            sellOneTx = min(sellOneTx, price-maxOneTx)
            maxTwoTx = max(maxTwoTx, price-sellOneTx)
        return maxTwoTx
