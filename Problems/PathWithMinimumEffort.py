import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Dijkstra's Algorithm
        lenRows = len(heights)
        lenColumns = len(heights[0])
        visited = {}
        priorityQueue = [(0,(0,0))]
        
        def getNeighbour(x,y):
            result = []
            
            if x+1 < lenRows: #Up
                result.append((x+1,y))
            if y+1 < lenColumns: #Right
                result.append((x,y+1))
            if x-1 >= 0: #Down
                result.append((x-1,y))
            if y-1 >= 0: #Left
                result.append((x,y-1))
                
            return result
        
        while priorityQueue:
            (effort, node) = heapq.heappop(priorityQueue)
            (nodeX, nodeY) = node
            
            if node in visited:
                continue
            
            if node == (lenRows-1, lenColumns-1):
                return effort
            
            visited[node] = effort
            for i in getNeighbour(nodeX, nodeY):
                if i not in visited:
                    
                    heapq.heappush(priorityQueue,(max(visited[node],abs(heights[nodeX][nodeY] - heights[i[0]][i[1]])),i))
