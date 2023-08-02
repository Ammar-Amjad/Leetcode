class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
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
                
    def connected(self, X, Y):
        return self.find(X) == self.find(Y)


class Solution:
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        m = len(isConnected[0])
        
        UF = UnionFind(n)
        No = n
        
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1 and UF.find(i) != UF.find(j):
                    No -= 1
                    UF.union(i, j)
        return No
        
    