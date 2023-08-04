class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj_list = defaultdict(list)
        
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
            
        seen = set()
        stack = [source]
        
        while stack:
            curr = stack.pop()
            
            if curr == destination:
                return True
            
            if curr in seen:
                continue
                
            seen.add(curr)
            
            for nei in adj_list[curr]:
                stack.append(nei)
                
        return False