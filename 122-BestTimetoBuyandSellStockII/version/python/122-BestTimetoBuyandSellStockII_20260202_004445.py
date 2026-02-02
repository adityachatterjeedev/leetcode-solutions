# Last updated: 2/2/2026, 12:44:45 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        total_prof = 0
4
5        for i in range(1, len(prices)):
6            if prices[i] > prices[i - 1]:
7                total_prof += (prices[i] - prices[i - 1])
8
9        return total_prof
10