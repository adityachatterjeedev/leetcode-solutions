# Last updated: 2/23/2026, 1:42:12 PM
1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        answer = prices.copy()
4
5        stack = []
6
7        for i, p in enumerate(prices):
8            while stack and stack[-1][0] >= p:
9                answer[stack.pop()[1]] -= p
10            stack.append((p, i))
11
12        return answer