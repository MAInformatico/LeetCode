class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = len(graph)
        set1 = [False for _ in range(nodes)]
        set2 = [False for _ in range(nodes)]
        
        for i in range(nodes):
            if set1[i] or set2[i]:
                continue
            if not self.DFS(i,set1,set2,graph):
                return False
        
        return True
    
    def DFS(self,current,set1,set2,graph):
        if (set1[current]):
            return not set2[current]
        
        set1[current] = True
        
        for i in graph[current]:
            if not self.DFS(i,set2,set1,graph):
                return False
        
        return True
