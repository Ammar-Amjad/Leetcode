class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, target):
            if target == 0:
                return 1
            
            Count = 0
            for j in range(i, len(coins)):
                if target - coins[j] >= 0:
                    Count += dfs(j, target - coins[j])
            return Count
        
        return dfs(0, amount)