class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [float('inf') for i in range(n)]
        prev[src] = 0
        
        for i in range(k + 1):
            tempP = prev[:]
            
            for u, v, cost in flights:
                if prev[u] == float('inf'):
                    continue
                
                if prev[u] + cost < tempP[v]:
                    tempP[v] = prev[u] + cost
                
            prev = tempP
            
        return prev[dst] if prev[dst] != float('inf') else -1
        
        
        