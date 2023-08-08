class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        
        for u, v, cost in times:
            adj_list[u].append((v, cost))
            
        
        visited = set()
        
        minHeap = []
        
        heapq.heappush(minHeap, (0, k))
        
        total_cost = 0
        
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            total_cost = max(total_cost, cost)
            
            if len(visited) == n:
                return total_cost
            
            for v, c in adj_list[node]:
                heapq.heappush(minHeap, (c + cost, v))
        
        return total_cost if len(visited) == n else -1