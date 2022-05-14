class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacentList = defaultdict(list)
        
        for i,j,l in times:
            adjacentList[i].append((l, j))
        
        visited=set()
        heap = [(0, k)]
        while heap:
            travelTime, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited)==n:
                return travelTime
            
            for time, adjacentNode in adjacentList[node]:
                if adjacentNode not in visited:
                    heapq.heappush(heap, (travelTime+time, adjacentNode))
                
        return -1
