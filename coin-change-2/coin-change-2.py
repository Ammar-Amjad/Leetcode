class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for i in range(amount + 1)] for _ in range(len(coins))]
        
        for row in range(len(coins) - 1, -1, -1):
            for col in range(amount + 1):
                if col == 0:
                    dp[row][col] = 1
                else:    
                    if col - coins[row] >= 0:
                        dp[row][col] += dp[row][col - coins[row]]

                    if row + 1 < len(coins):
                        dp[row][col] += dp[row + 1][col]
                        
        return dp[0][amount]
                    