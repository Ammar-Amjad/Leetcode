class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        for n in nums:
            dic[n] += n

        @cache
        def dfs(num):
            if num <= 0:
                return 0 

            return max(dfs(num - 2) + dic[num], dfs(num - 1))

        return dfs(max(nums))