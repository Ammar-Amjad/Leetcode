class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                xr, yr = yr, xr
            self.parent[yr] = xr
            self.rank[xr] += self.rank[xr] == self.rank[yr]



class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n)
        # Add wells as edges from 0
        edges = [(cost, 0, i+1) for i, cost in enumerate(wells)]
        edges += [(cost, i, j) for i, j, cost in pipes]

        total_cost = 0
        for cost, i, j in sorted(edges):
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                total_cost += cost

        return total_cost
