class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        N = len(sticks)
        heapq.heapify(sticks) 
        res = 0
        
        while len(sticks) > 1:
            val = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += val
            heapq.heappush(sticks, val)
        return res
        
        # O(N Log N)
        # O(N)