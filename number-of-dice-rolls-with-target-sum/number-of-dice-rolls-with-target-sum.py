class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dfs(i, j, t):
            if i == 0 and t == 0:
                return 1
            elif i == 0 or t == 0:
                return 0
            
            res = 0
            for j in range(1, k + 1):
                res += dfs(i - 1, j, t - j) 
            return res
        
        res = 0
        for j in range(1, k + 1):
            res += dfs(n - 1, j, target - j)
        
        return res % (10**9 + 7)