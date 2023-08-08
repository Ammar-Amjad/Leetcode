class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for x, y, cost in times:
            adj_list[x].append((y, cost))
            
        
        minheap = []
        
        heapq.heappush(minheap, (0, k))
        
        visited = set()
        total_cost = 0 
        
        while minheap:
            cost, node = heapq.heappop(minheap)
            
            if len(visited) == n:
                return total_cost
            
            if node in visited:
                continue
            
            visited.add(node)
            
            total_cost = max(total_cost, cost)
                                      

            for nei in adj_list[node]:
                heapq.heappush(minheap, (cost + nei[1], nei[0]))
                
        return total_cost if len(visited) == n else -1