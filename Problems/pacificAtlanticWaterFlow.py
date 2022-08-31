class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row,column = len(heights),len(heights[0])
        result = []

        def DFS(i,j,previous,mode):
            
            if i==row or i<0 or j==column or j<0 or heights[i][j]<previous:
                return
            
            if mode=="pac":
                if (i,j) in self.pac:
                    return
                self.pac.add((i,j))
            else:
                if (i,j) in self.atl:
                    return
                self.atl.add((i,j))
            
            DFS(i+1,j,heights[i][j],mode)
            DFS(i-1,j,heights[i][j],mode)
            DFS(i,j+1,heights[i][j],mode)
            DFS(i,j-1,heights[i][j],mode)
            
        self.atl, self.pac = set(),set()
        
        for i in range(row):
            DFS(i,0,-1,"pac")
        for j in range(column):
            DFS(0,j,-1,"pac")
        for i in range(row):
            DFS(i,column-1,-1,"atl")
        for j in range(column):
            DFS(row-1,j,-1,"atl")
        
        for ite in self.atl:
            if ite in self.pac:
                i,j = ite
                result.append([i,j])
            
        return result
