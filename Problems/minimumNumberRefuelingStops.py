class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target,0])
        result, previous, tank = 0, 0, startFuel
        heap = []
        
        for current, fuel in stations:
            tank -= current - previous
            while len(heap) != 0 and tank < 0:
                tank += -heapq.heappop(heap)
                result += 1
            if tank < 0:
                return -1
            heapq.heappush(heap, -fuel)
            previous = current
        return result
