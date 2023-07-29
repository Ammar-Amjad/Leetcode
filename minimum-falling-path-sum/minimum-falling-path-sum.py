class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])

        Brow = mat[n - 1]
        for i in range(n - 2, -1, -1):
            Arow = [0 for i in range(m - 1, -1, -1)]
            for j in range(m):
                if j == 0:
                    Arow[j] = min(Brow[j], Brow[j + 1])
                elif j == m - 1:
                    Arow[j] = min(Brow[j], Brow[j - 1])
                else:
                    Arow[j] = min(Brow[j - 1], Brow[j], Brow[j + 1])
                Arow[j] += mat[i][j]
            Brow = Arow 
        return min(Brow)
