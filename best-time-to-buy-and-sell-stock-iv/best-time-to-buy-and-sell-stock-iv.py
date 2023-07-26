class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i, BS, D):
            
            if D == 0:
                return 0
            
            if i == len(prices) - 1:
                if BS:
                    return 0
                else:
                    return prices[i]
            
            if BS:
                return max(dfs(i + 1, not BS, D) - prices[i], dfs(i + 1, BS, D))
            else:
                return max(dfs(i + 1, not BS, D - 1) + prices[i], dfs(i + 1, BS, D))
            
        return dfs(0, True, k)
    