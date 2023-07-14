class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}
        
        def dfs(i):
            if i <= 1:
                return cost[i] 
            if i not in dp:
                dp[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
            return dp[i]
        n = len(cost) 
        cost.append(0)
        return dfs(n)
