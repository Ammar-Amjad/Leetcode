class Solution:
    def __init__(self):
        self.dp = {}
    
    def climbStairs(self, n: int) -> int:    
        
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n not in self.dp:
            self.dp[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        
        return self.dp[n]