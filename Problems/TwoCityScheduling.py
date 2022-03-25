class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diffCost = sorted([b - a for a, b in costs])
        costsA = sum(i for i, _ in costs)
        return costsA + sum(diffCost[:len(diffCost)//2])
