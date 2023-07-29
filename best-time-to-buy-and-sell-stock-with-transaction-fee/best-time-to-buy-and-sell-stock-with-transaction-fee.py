class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @cache
        def dfs(i, BS):
            if i == len(prices) - 1:
                if BS == True:
                    return 0
                else:
                    return prices[i]
                
            if BS:
                return max(dfs(i + 1, not BS) - prices[i] - fee, dfs(i + 1, BS))
            else:
                return max(dfs(i + 1, not BS) + prices[i], dfs(i + 1, BS))
        
        return dfs(0, True)