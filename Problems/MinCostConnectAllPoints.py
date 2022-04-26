class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prim's Algorithm
        ManhattanDistance = 0
        points = list(map(lambda i: tuple(i), points))
        notVisited = set(points)
        pq = [(0, points[0])]
        while notVisited:
            distance, i = heapq.heappop(pq)
            if i not in notVisited:
                continue
            notVisited.remove(i)
            ManhattanDistance += distance
            for j in notVisited:
                heapq.heappush(pq, (abs(j[0] - i[0]) + abs(j[1] - i[1]), j))
        return ManhattanDistance
