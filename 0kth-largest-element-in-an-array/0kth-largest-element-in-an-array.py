import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        
        for i in range(len(nums)):
            
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, nums[i])   
            
            elif nums[i] >= maxHeap[0]: 
                if len(maxHeap) >= k:
                    heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, nums[i]) 
        return maxHeap[0] 
            