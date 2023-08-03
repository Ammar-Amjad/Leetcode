class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:
        if edges == []:
            return True
        
        graph = defaultdict(list)
        
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
            
        visited = [False for i in range(n)]
        
        stack = [src]
        
        while stack:
            curr = stack.pop()
            
            if curr == dest:
                return True
            
            for nei in graph[curr]:
                if not visited[nei]:
                    stack.append(nei)
                    visited[nei] = True        
            
        return False