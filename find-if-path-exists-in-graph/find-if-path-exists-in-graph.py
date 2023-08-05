class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> bool:
        
        adj_list = defaultdict(list)
        
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
            
        queue = deque([])
        queue.append(src)
        
        visited = set()
        
        while queue:
            curr = queue.popleft() 
            if curr == dst:
                return True
            
            if curr in visited:
                continue
            
            for nei in adj_list[curr]:
                if nei not in visited:
                    visited.add(curr)
                    queue.append(nei)
                
        return False