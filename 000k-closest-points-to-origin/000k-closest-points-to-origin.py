class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x, y):
            return abs(((x ** 2) + (y ** 2)) ** 0.5)
        
        heap = []
        
        for i in range(len(points)):
            new_dist = -1 * dist(points[i][0], points[i][1])
            if len(heap) < k:
                heapq.heappush(heap, (new_dist, points[i][0], points[i][1]))                
            elif heap[0][0] < new_dist:
                heapq.heappop(heap)
                heapq.heappush(heap, (new_dist, points[i][0], points[i][1]))
            if len(heap) > k:
                heapq.heappop(heap) 
        res = []
        while heap:
            new_dist, x, y = heapq.heappop(heap)
            res.append((x, y))
            
        return res
        # O(N log N)
        # O(N)