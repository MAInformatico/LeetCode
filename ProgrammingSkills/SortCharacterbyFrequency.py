class Solution:
    def frequencySort(self, s: str) -> str:
        maxHeap = []
        result = ""
        
        frequencies = Counter(s)
        
        for key,value in frequencies.items():
            heapq.heappush(maxHeap, (-value, key))
            
        while maxHeap:
            num = -1 * maxHeap[0][0]
            result += num*maxHeap[0][1]
            heapq.heappop(maxHeap)
            
        return result
