class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        self.dp = {len(cost): 0, len(cost) - 1: cost[len(cost) - 1]}
        
        def dfs(i):
            if i in self.dp:
                return self.dp[i]
            self.dp[i] = min(dfs(i + 1), dfs(i + 2)) + cost[i]
            
            return self.dp[i]
        dfs(0)
        
        return min(self.dp[0], self.dp[1]) 
        