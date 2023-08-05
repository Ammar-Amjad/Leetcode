class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        src = 0
        dst = len(graph) - 1
        
        queue = deque()
        queue.append([src])

        res = []
        
        while queue:
            curr = queue.popleft()
            
            if curr[-1] == dst:
                res.append(curr) 
                continue
            
            for nei in graph[curr[-1]]:
                queue.append(curr + [nei])
        
        return res