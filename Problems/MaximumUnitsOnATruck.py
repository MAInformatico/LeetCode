class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result = 0
        queue = deque(sorted(boxTypes, key=lambda x: x[1], reverse=True))
        
        while queue and truckSize:
            boxes, units = queue.popleft()
            while boxes:
                if boxes <= truckSize:
                    result += boxes * units
                    truckSize -= boxes
                    boxes = 0
                else:
                    boxes -= 1
        
        return result
