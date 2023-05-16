class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
    
            if p1 == p2:
                return 0

            if rank[p1] <= rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
        # time complexity: O(E * alpha(E)) = O(E) * O(alpha(E)) the reverse ackerman function
        # space complexity: O(V)