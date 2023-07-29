class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        @cache
        def dfs(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            
            score1, score2 = float('inf'), float('inf')
            
            if i + 1 < n:
                score1 = dfs(i + 1, j)
                
            if j + 1 < m:
                score2 = dfs(i, j + 1)
                
            return grid[i][j] + min(score1, score2)
        
        return dfs(0, 0)