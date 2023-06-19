class Solution:
    def __init__(self):
        self.dp = {0: 1, 1: 1}
    
    def climbStairs(self, n: int) -> int:    
        
        
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]