class Solution:
    def minCostII(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        dp = mat[0].copy()
        
        for i in range(1, rows):        
            next_dp = [0 for i in range(cols)]
            for j in range(cols):
                if j == 0:
                    next_dp[j] = mat[i][j] + min(dp[j + 1:]) 
                    
                elif j == cols - 1:
                    next_dp[j] = mat[i][j] + min(dp[:j])
                
                else:
                    next_dp[j] = mat[i][j] + min(dp[:j] + dp[j + 1:])
            dp = next_dp
            
        return min(dp)
                