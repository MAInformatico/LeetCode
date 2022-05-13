class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inComing = set([i for j,i in edges])
        return list(set(range(n)).difference(inComing))
