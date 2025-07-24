# Last updated: 7/24/2025, 1:31:47 PM
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        res = float('inf')
        left = 0
        curr_or = 0

        for right in range(n):
            curr_or |= nums[right]
            while left <= right and curr_or >= k:
                res = min(res, right - left + 1)

                left += 1
                curr_or = 0
                for i in range(left, right + 1):
                    curr_or |= nums[i]

        return res if res != float('inf') else -1