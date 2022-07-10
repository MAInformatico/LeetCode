class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        
        if length == 1:
            return cost[0]
        
        if length == 2:
            return min(cost[0], cost[1])
        
        x = cost[0]
        y = cost[1]
        
        for i in range(2,length):
            z = min(x,y) + cost[i]
            x = y
            y = z
        
        return min(x,y)
