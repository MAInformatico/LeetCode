class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        init = 0
        end = len(arr) - 1
        middle = init + (end - init)//2
        
        while init < end:
            if arr[middle] < arr[middle + 1]:
                init = middle + 1
            else:
                end = middle
            middle = init + (end - init)//2
        
        return init
