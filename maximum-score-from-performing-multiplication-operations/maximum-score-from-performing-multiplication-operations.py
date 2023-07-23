class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dfs(st, end, i):
            if i == len(multipliers):
                return 0
            
            score = max((nums[st] * multipliers[i]) + dfs(st + 1, end, i + 1),
                         (nums[end] * multipliers[i]) + dfs(st, end - 1, i + 1))
            
            return score
        
        return dfs(0, len(nums) - 1, 0)