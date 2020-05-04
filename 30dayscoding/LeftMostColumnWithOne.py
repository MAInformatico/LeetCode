# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ldimension = binaryMatrix.dimensions()
        rows = ldimension[0]
        cols = ldimension[1]
        
        if rows == 0 or cols == 0:
            return -1
        
        result = -1
        iterrows = 0
        itercols = cols - 1
        while(iterrows<rows and itercols>=0):
            if(binaryMatrix.get(iterrows,itercols) == 1):
                result = itercols
                itercols -= 1
            else:
                iterrows += 1
        return result
