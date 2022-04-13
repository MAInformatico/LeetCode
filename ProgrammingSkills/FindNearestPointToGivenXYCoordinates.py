class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        result = -1
        CurrentManhattanDistance = -1
        for i in points:
            if i[0] == x or i[1] == y:
                if CurrentManhattanDistance == -1 or (abs(i[0] - x) + abs(i[1] - y)) < CurrentManhattanDistance:
                    CurrentManhattanDistance = abs(i[0] - x) + abs(i[1] - y)
                    result = points.index(i)
        return result
