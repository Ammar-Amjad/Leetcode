class Solution:
    def minCostII(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        dp = [[0 for i in range(cols)] for j in range(rows)]
        dp[0] = mat[0]
        
        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = mat[i][j] + min(dp[i - 1][j + 1:]) 
                    
                elif j == cols - 1:
                    dp[i][j] = mat[i][j] + min(dp[i - 1][:j])
                
                else:
                    dp[i][j] = mat[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
            
        return min(dp[rows - 1])
                