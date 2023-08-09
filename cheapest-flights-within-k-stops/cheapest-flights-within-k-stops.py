class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf') for i in range(n)]
        prev[src] = 0
        
        for i in range(k + 1):
            curr = prev[:]
            for e1, e2, cost in flights:
                if prev[e1] == float('inf'):
                    continue
                    
                if prev[e1] + cost < curr[e2]:
                    curr[e2] = prev[e1] + cost
            prev = curr
        
        return prev[dst] if prev[dst] != float('inf') else -1
                    
            