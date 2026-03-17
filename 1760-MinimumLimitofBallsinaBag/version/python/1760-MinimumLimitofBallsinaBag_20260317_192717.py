# Last updated: 3/17/2026, 7:27:17 PM
1class Solution:
2    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
3        l, r = 1, max(nums)  # max possible size is max in nums
4
5        res = r
6
7        while l <= r:
8            mid = (l + r) // 2
9
10            # calculate how many splits are needed
11            operations_needed = sum((num - 1) // mid for num in nums)
12
13            if operations_needed <= maxOperations:
14                res = mid
15                r = mid - 1
16            else:
17                l = mid + 1
18
19        return res