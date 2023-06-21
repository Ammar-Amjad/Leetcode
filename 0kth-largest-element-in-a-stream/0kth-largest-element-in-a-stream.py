import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        heapq.heapify(self.minHeap)
        
        for i in range(len(nums)):
            self.add(nums[i])
        
        return None
        
    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            
        elif val >= self.minHeap[0]:
            if len(self.minHeap) >= self.k:
                heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)