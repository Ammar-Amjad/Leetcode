class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            dp[i] = max(dfs(i - 2) + nums[i], dfs(i - 1))
        
            return dp[i]

        return dfs(len(nums) - 1)