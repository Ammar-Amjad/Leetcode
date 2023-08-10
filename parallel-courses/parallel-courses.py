class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
 
        adj_list = defaultdict(list)
        in_degree = {i: 0 for i in range(1, n + 1)}
        
        for e1, e2 in relations:
            adj_list[e1].append(e2)
            in_degree[e2] += 1 
        queue = deque()
        
        for k, v in in_degree.items():
            if v == 0:
                queue.append((k, 1))
        print(queue)
        res = 0
        course_taken = 0
        
        while queue:
            node, Len = queue.popleft()
            res = Len
            course_taken += 1
            
            for nei in adj_list[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append((nei, Len + 1))
        
        return res if course_taken == n else -1
        