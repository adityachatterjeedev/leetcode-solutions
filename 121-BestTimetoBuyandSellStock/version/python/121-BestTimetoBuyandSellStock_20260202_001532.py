# Last updated: 2/2/2026, 12:15:32 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        max_prof = 0
4        buy = prices[0]
5
6        for right in range(1, len(prices)):
7            if prices[right] < buy:
8                buy = prices[right]
9            else:
10                max_prof = max(max_prof, prices[right] - buy)
11        
12        return max_prof