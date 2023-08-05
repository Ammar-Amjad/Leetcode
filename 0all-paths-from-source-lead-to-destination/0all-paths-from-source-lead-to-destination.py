class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        graph = defaultdict(set)
        visited = set()

        for x, y in edges:
            graph[x].add(y)
            
        @cache
        def dfs(node):
            if node in visited:
                return False
            
            if not graph[node]:
                return node == destination
            
            visited.add(node)

            for child in graph[node]:
                if not dfs(child):
                    return False

            visited.remove(node)
            return True

        return dfs(source)