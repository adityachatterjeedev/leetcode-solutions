# Last updated: 3/17/2026, 7:28:10 PM
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
11            operations_needed = 0
12
13            for num in nums:
14                operations_needed += (num - 1) // mid
15
16            if operations_needed <= maxOperations:
17                res = mid
18                r = mid - 1
19            else:
20                l = mid + 1
21
22        return res