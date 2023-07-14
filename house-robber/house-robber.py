class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = { }
        
        def dfs(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            if i not in dp:
                dp[i] = max(dfs(i - 1), dfs(i - 2) + nums[i]) 
            return dp[i]
        
        return dfs(len(nums) - 1)