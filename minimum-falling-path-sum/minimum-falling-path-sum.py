class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])
        @cache
        def dfs(i, j):
            if i == n - 1:
                return mat[i][j]
            
            score = float('inf')
            if j - 1 >= 0:
                score = min(score, dfs(i + 1, j - 1))
            if j + 1 < m:
                score = min(score, dfs(i + 1, j + 1))
            score = min(score, dfs(i + 1, j))
            return mat[i][j] + score
        
        min_path = float('inf')
        for x in range(m):
            min_path = min(min_path, dfs(0, x))
        return min_path 