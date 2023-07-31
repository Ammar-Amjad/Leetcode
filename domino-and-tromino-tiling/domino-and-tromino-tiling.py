class Solution:
    def numTilings(self, n: int) -> int:
        print(n)
        dp = [0 for _ in range(n + 1)]
        if n == 1:
            return 1
        dp[1] = 1
        if n == 2:
            return 2
        dp[2] = 2
        if n == 3:
            return 5
        dp[3] = 5
        for i in range(4, n + 1):
            dp[i] = (dp[i - 3] + (dp[i - 1] * 2))
        return (dp[n]) % (10**9 + 7)
        