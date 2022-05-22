class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        if arr[-1] <= k:
            return k + len(arr)
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return k + left
