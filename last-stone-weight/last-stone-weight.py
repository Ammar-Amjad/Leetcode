import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            A = heapq.heappop(maxHeap) 
            B = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, abs(A - B) * -1)
            
        return maxHeap[0] * -1
        
        