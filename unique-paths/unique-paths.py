class Solution:
    def __init__(self):
        self.dp = {}

    def uniquePaths(self, m: int, n: int) -> int:
        
        Arow = [1 for i in range(n)]
        temp = [0 for i in range(n)]
        temp[0] = 1
        Brow = temp[:]
        for row in range(1, m):
            Brow = temp[:]
            for col in range(1, n):
                Brow[col] = Arow[col] + Brow[col - 1]
            Arow = Brow
            
        return Arow[n - 1]