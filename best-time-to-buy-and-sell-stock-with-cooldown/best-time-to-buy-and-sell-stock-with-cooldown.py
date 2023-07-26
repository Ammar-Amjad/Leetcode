class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        BSC = ['Buy', 'Sell', 'Cooldown']
        @cache
        def dfs(i, Bi):
            if i == len(prices) - 1:
                if BSC[Bi] == 'Buy':
                    return 0
                elif BSC[Bi] == 'Sell':
                    return prices[i]
                else:
                    return 0
                
            if BSC[Bi] == 'Buy':
                return max(dfs(i + 1, (Bi + 1) % 3) - prices[i], dfs(i + 1, Bi))
            elif BSC[Bi] == 'Sell':
                return max(dfs(i + 1, (Bi + 1) % 3) + prices[i], dfs(i + 1, Bi))
            else:
                return dfs(i + 1, (Bi + 1) % 3)
                
        return dfs(0, 0)