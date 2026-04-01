# Last updated: 4/1/2026, 4:12:15 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        #dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
4        dp = [-1] * len(cost)
5        dp[-1] = cost[-1]
6        dp[-2] = cost[-2]
7        for i in range(len(cost) - 3, -1, -1):
8            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
9
10        return min(dp[0], dp[1])