class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        
        def dfs(target):
            if target in dp:
                return dp[target]
            
            if target < 0:
                return -1
            
            if target == 0:
                return 0
            
            val = []
            for c in coins:
                temp = dfs(target - c) 
                if temp != -1:
                    val.append(temp)
            dp[target] = 1 + min(val) if val != [] else -1
            return dp[target]
        
        return dfs(amount)