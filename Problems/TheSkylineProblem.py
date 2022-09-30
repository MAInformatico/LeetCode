class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.append([inf, inf, 0]) # sentinel 
        
        result, priorityQueue = [], [] # max-heap 
        for leftcoordX, rightcoordX, heightX in buildings: 
            while priorityQueue and -priorityQueue[0][1] < leftcoordX: 
                _, rightcoordY = heappop(priorityQueue) 
                while priorityQueue and -priorityQueue[0][1] <= -rightcoordY: heappop(priorityQueue) 
                heightY = priorityQueue[0][0] if priorityQueue else 0
                result.append((-rightcoordY, -heightY))
            if 0 < heightX and (not priorityQueue or -priorityQueue[0][0] < heightX): 
                if result and result[-1][0] == leftcoordX: result.pop()
                result.append((leftcoordX, heightX))
            heappush(priorityQueue, (-heightX, -rightcoordX))
        return result
