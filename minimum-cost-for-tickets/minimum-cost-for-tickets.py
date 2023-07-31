class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        md = days[len(days) - 1]
        dp = [0 for _ in range(md + 1)]

        i = 0
        for d in range(1, md + 1):
            if d < days[i]:
                dp[d] = dp[d - 1]
            else:
                i += 1
                dp[d] = min(dp[d - 1] + costs[0], dp[max(0, d - 7)] + costs[1], dp[max(0, d - 30)] + costs[2])

        return dp[md]            

