class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      
        def dfs(node):
            if node in setVisited:
                return
              
            setVisited.add(node)
            
            for i in rooms[node]:
                dfs(i)
                
        setVisited = set()
        dfs(0)
        return True if len(setVisited) == len(rooms) else False
