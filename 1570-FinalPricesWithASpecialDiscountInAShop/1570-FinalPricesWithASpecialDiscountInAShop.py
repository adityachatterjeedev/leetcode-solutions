# Last updated: 7/7/2026, 6:35:57 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, p in enumerate(prices):
            while stack and stack[-1][0] >= p:
                prices[stack.pop()[1]] -= p
            stack.append((p, i))

        return prices