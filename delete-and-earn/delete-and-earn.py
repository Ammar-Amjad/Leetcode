class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        max_num = -float('inf')
        
        for num in nums:
            dic[num] += num
            if num > max_num:
                max_num = num
        
        dp = [0 for _ in range(max_num + 1)]
        
        dp[0] = 0
        dp[1] = dic[1]
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 2] + dic[i], dp[i - 1])

        return dp[max_num]
        