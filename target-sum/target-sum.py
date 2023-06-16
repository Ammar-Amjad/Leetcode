class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        
        @cache        
        def dfs(Sum, i):
            if n == i:
                if Sum == target:
                    return 1
                return 0
            
            return dfs(Sum + nums[i], i + 1) + dfs(Sum - nums[i], i + 1)
        
        return dfs(0, 0)