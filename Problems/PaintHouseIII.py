class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def minCostDynamicProgramming(i, previousColor, groups):
            if i == m:
                return 0 if groups == target else float('inf')
            
            if houses[i] != 0:
                return min_cost_helper(i + 1, houses[i], groups + int(previousColor != houses[i]))
            
            total = float('inf')
            for color in range(1, n + 1):
                total = min(total, cost[i][color - 1] + minCostDynamicProgramming(i + 1, color, groups + int(previousColor != color)))
            
            return total
        
        result = minCostDynamicProgramming(0, -1, 0)
        return result if result != float('inf') else -1
