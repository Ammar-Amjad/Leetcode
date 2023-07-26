class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def dfs(i, target):
            if (i, target) in dp:
                return dp[(i, target)]
            if target == 0:
                return 1
            
            dp[(i, target)] = 0
            for j in range(i, len(coins)):
                if target - coins[j] >= 0:
                    dp[(i, target)] += dfs(j, target - coins[j])
             
            return dp[(i, target)]
        
        return dfs(0, amount)