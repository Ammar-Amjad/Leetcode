class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        mArea = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
                    mArea = max(mArea, dp[i][j])
        
        return mArea * mArea