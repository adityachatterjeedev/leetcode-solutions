# Last updated: 4/8/2026, 3:13:08 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        dp = [0] * (n + 1)
4        for i in range(n + 1):
5            dp[i] = dp[i >> 1] + (i & 1)
6        return dp