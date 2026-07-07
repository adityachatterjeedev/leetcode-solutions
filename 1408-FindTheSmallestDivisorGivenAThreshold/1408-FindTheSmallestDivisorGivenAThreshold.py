# Last updated: 7/7/2026, 6:36:00 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        ma = max(nums)

        if threshold == len(nums):
            return ma
        
        if threshold >= sum(nums):
            return 1

        l, r = 2, ma - 1

        while l <= r:
            mid = (l + r) // 2

            val = 0
            for num in nums:
                val += (num // mid) + (num % mid != 0)

            if val <= threshold:
                r = mid - 1
            else:
                l = mid + 1

        return l