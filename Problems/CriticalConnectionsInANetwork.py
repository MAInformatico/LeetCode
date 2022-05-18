class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for node1, node2 in connections:
            graph[node1].append(node2), graph[node2].append(node1)
        
        arrivalTime = [None]*n
        result = []
        
        def dfs(node = 0, parent = -1, time = 1):
            if arrivalTime[node]: return
            arrivalTime[node] = time
            for i in graph[node]:
                if i == parent: continue
                dfs(i,node,time + 1)
                if arrivalTime[i] == time + 1:
                    result.append((node,i))
                else:
                    arrivalTime[node] = min(arrivalTime[node], arrivalTime[i])
            return result
        
        return dfs()
