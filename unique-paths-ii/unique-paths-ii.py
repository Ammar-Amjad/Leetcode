class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        m = len(Grid)
        n = len(Grid[0])
        
        Arow = [0 for _ in range(n)]
        Flag = False
        
        for j in range(n):
            if Grid[0][j] == 1:
                Arow[j] = 0
                Flag = True
            else:
                if not Flag:
                    Arow[j] = 1
                else:
                    Arow[j] = 0
        
        for i in range(1, m):
            Brow = [0 for _ in range(n)]
            for j in range(n):
                if j == 0:
                    if Grid[i][0] == 1 or Arow[0] == 0:
                        Brow[0] = 0
                    else:
                        Brow[0] = 1
                else:
                    if Grid[i][j] == 1:
                        Brow[j] = 0
                    else:
                        Brow[j] = Brow[j - 1] + Arow[j]
            
            Arow = Brow
            
        return Arow[n - 1]
        