# Last updated: 7/7/2026, 6:35:50 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        total = sum(nums)
        count = 0
        left = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if 2 * left >= total:
                count += 1

        return count