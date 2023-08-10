class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         Kahn's algorithm for topological sort
# 1- add indegree 0 nodes to queue
# 2- reduce indegree of nei by 1 of poped node
# 3- add poped node to result
# 4- return res
        in_degree = {i: 0 for i in range(numCourses)}
        adj_list = defaultdict(list)
        
        for p1, p2 in prerequisites:
            adj_list[p2].append(p1)
            in_degree[p1] += 1
        
        queue = deque([])
        
        for i in range(numCourses):
            if in_degree[i] == 0:        
                queue.append(i)
        
        res = []
        while queue:
            node = queue.popleft()
            
            res.append(node)
            for nei in adj_list[node]:
                in_degree[nei] -= 1
                
                if in_degree[nei] == 0:
                    queue.append(nei)
            
        return res if len(res) == numCourses else []
            