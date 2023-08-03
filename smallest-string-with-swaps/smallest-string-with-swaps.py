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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        UF = UnionFind(n)

        for p1, p2 in pairs:
            UF.union(p1, p2)

        groups_i = defaultdict(list)
        groups_ch = defaultdict(list)

        for i in range(n):
            group = UF.find(i)
            groups_i[group].append(i)
            groups_ch[group].append(s[i])

        res = [''] * n 
        for g in groups_i.keys():
            l = sorted(groups_i[g])
            c = sorted(groups_ch[g])
            for i, ch in zip(l, c):
                res[i] = ch

        return ''.join(res)




