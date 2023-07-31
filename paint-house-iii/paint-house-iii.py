class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @cache
        def dfs(i, nc, t):
            if t > target: 
                return float('inf')
            if i == m:
                return 0 if t == target else float('inf')
                
            if houses[i] != 0:
                return dfs(i + 1, houses[i] - 1, t + (nc != houses[i] - 1))
            
            return min(cost[i][c] + dfs(i + 1, c, t + (nc != c)) for c in range(n))
                
        
        res = min(dfs(0, n, 0) for nc in range(n))
        return -1 if res == float('inf') else res
        