# Last updated: 7/7/2026, 6:35:48 PM
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxRange = 0
        total = 0

        for num in nums:
            l = [int(d) for d in list(str(num))]
            n_range = max(l) - min(l)

            if n_range > maxRange:
                maxRange = n_range
                total = num
            elif n_range == maxRange:
                total += num


        return total