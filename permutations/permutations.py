class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        L = len(nums)

        def dfs(i):
            if i == len(nums):
                ans.append(nums[:])
                return 
            
            for j in range(i, L):
                nums[j], nums[i] = nums[i], nums[j]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]
                
        dfs(0)

        return ans