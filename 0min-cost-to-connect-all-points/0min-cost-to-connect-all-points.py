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

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                costs.append((abs(x1 - x2) + abs(y1 - y2), i, j))
        
        
        costs.sort(key = lambda x: x[0])
         
        
        UF = UnionFind(len(points))
        
        total = 0
        count = 0
        for cost, x, y in costs:
            if count == len(points) - 1:
                break
                
            if UF.find(x) != UF.find(y): 
                count += 1
                total += cost
                UF.union(x, y)
        
        return total
        