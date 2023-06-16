class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        
        dp = {}     
        def dfs(Sum, i):
            if (Sum, i) in dp:
                return dp[(Sum, i)]

            if n == i:
                if Sum == target:
                    return 1
                return 0

            pos = dfs(Sum + nums[i], i + 1) 
            neg = dfs(Sum - nums[i], i + 1)

            dp[(Sum, i)] = pos + neg

            return dp[(Sum, i)]
        
        return dfs(0, 0)