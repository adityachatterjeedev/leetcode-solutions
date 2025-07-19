# Last updated: 7/19/2025, 12:59:16 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)

        if length in [0,1]:
            return 0
        
        result = 0

        left, right = 0, 1

        while right < length:
            if prices[right] < prices[left]:
                left = right
            else:
                result = max(result, prices[right] - prices[left])

            right += 1

        return result