import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = nums[:k]
        self.heapSize = len(self.heap)
        heapq.heapify(self.heap)
        
        for i in range(k,len(nums)):
            if i >self.heap[0]:
                heapq.heapreplace(self.heap,nums[i])

    def add(self, val: int) -> int:
        
        if self.heapSize < self.k:
            heapq.heappush(self.heap,val)
            self.heapSize += 1
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap,val)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
