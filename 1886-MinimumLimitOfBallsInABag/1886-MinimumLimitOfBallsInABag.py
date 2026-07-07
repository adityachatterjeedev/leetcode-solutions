# Last updated: 7/7/2026, 6:35:54 PM
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)  # max possible size is max in nums

        res = r

        while l <= r:
            mid = (l + r) // 2

            # calculate how many splits are needed
            operations_needed = 0

            for num in nums:
                operations_needed += (num - 1) // mid

            if operations_needed <= maxOperations:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res