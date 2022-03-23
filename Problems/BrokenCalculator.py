class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        def count(target,startValue):
            if startValue >= target:
                return startValue - target
            
            elif target % 2 != 0:
                return 1 + count(target+1, startValue)
            
            else:
                return 1 + count(target/2, startValue)
        
        result = count(target,startValue)
        
        return int(result)
