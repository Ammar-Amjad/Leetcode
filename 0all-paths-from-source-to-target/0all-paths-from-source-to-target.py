class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        res = []
        seen = set()
        def dfs(i, temp):
            if i == n - 1:
                res.append(temp[:])
            
            for nei in graph[i]:
                if nei not in seen:
                    seen.add(nei)
                    temp.append(nei)
                    dfs(nei, temp)
                    temp.pop()
                    seen.remove(nei)
        
        dfs(0, [0])
        return res