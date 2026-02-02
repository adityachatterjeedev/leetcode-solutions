# Last updated: 2/2/2026, 12:11:16 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        max_prof = 0
4        left, right = 0, 1
5        while right < len(prices):
6            if prices[right] < prices[left]:
7                left = right
8            else:
9                max_prof = max(max_prof, prices[right] - prices[left])
10            right += 1
11        
12        return max_prof