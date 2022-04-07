class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        elif len(stones) == 1:
            return stones[0]
        
        elif len(stones) == 2:
            return abs(stones[0] - stones[1])
        
        else:
            stones.sort()
            maxValue = max(stones)
            stones.remove(maxValue)
            secondMaxValue = max(stones)
            stones.remove(secondMaxValue)
                
            if maxValue != secondMaxValue:
                difference = abs(maxValue - secondMaxValue)
                stones.append(difference)
            
            result = self.lastStoneWeight(stones)
            return result
