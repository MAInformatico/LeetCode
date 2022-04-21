class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [y for (x,y) in sorted([(bin(arr[i]).count('1'), arr[i]) for i in range(len(arr))])]
