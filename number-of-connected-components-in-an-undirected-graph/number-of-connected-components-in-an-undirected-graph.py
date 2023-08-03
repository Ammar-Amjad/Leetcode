class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    
    def Find(self, X):
        if X == self.root[X]:
            return X
        self.root[X] = self.Find(self.root[X])
        return self.root[X]
    
    def Union(self, X, Y):
        rootX = self.Find(X)
        rootY = self.Find(Y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootY] < self.rank[rootX]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
         
        UF = UnionFind(n)
        
        for e1, e2 in edges:
            if UF.Find(e1) != UF.Find(e2):
                UF.Union(e1, e2)
                n -= 1
        
        return n