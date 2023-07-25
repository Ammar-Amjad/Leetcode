class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(target):
            if target < 0:
                return -1
            
            if target == 0:
                return 0
            
            val = []
            for c in coins:
                temp = dfs(target - c) 
                if temp != -1:
                    val.append(temp)
            return 1 + min(val) if val != [] else -1
        
        return dfs(amount)