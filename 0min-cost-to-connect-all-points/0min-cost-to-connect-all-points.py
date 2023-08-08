import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        heap = [(0, 0)]

        visited = [False for i in range(n)]

        cost = 0
        edges = 0

        while edges < n:
            weight, curr = heapq.heappop(heap)

            if visited[curr]:
                continue
            
            visited[curr] = True
            cost += weight
            edges += 1

            for node in range(n):
                if not visited[node]:
                    nCost = abs(points[curr][0] - points[node][0]) + abs(points[curr][1] - points[node][1])
                    heapq.heappush(heap, (nCost, node))

        return cost
        
        
        
        
        
        
        
        
        
        
        
        