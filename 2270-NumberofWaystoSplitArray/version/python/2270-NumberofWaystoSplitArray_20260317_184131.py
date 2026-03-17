# Last updated: 3/17/2026, 6:41:31 PM
1class Solution:
2    def waysToSplitArray(self, nums: List[int]) -> int:
3
4        total = sum(nums)
5        count = 0
6        left = 0
7        for i in range(len(nums) - 1):
8            left += nums[i]
9            if 2 * left >= total:
10                count += 1
11
12        return count