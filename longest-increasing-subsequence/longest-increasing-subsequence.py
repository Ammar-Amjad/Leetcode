class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i): 
            val = 1
            
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    val = max(val, 1 + dfs(j))
            
            return val  
        
        return max([dfs(i) for i in range(len(nums))])
        