class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        
    def find(self, X):
        if X == self.root[X]:
            return X
        self.root[X] = self.find(self.root[X])
        return self.root[X]
    
    def union(self, X, Y):
        rootX = self.find(X)
        rootY = self.find(Y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootY] < self.rank[rootX]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        UF = UnionFind(n)
        
        for t, e1, e2 in logs:
            if UF.find(e1) != UF.find(e2):
                UF.union(e1, e2)
                n -= 1
                if n == 1:
                    return t
        
        return -1
                
                
                