class Solution:
    def maxArea(self, height: List[int]) -> int:        
        areas = []
        
        while len(height) != 0:
            firstBorder = height[0]

            secondBorder = height[-1]

            localArea = min(firstBorder,secondBorder)*(len(height)-1)

            areas.append(localArea)

            if secondBorder < firstBorder:
                height.pop()
            else:
                height.remove(firstBorder)
	
        return max(areas)
