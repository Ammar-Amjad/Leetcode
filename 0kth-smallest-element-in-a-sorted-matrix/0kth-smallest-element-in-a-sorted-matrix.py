class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        rLen = len(matrix)
        cLen = len(matrix[0])
        
        for i in range(rLen):
            for j in range(cLen):
                heapq.heappush(heap, -1 * matrix[i][j]) 
                if len(heap) > k:
                    heapq.heappop(heap)
                    
        return heapq.heappop(heap) * -1
        
        # O(NlogK)
        # O(K)