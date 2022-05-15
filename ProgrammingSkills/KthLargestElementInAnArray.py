class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = [-i for i in nums]
        heapq.heapify(result)
        for _ in range(k-1):
            heapq.heappop(result)
        
        return heapq.heappop(result)* -1
