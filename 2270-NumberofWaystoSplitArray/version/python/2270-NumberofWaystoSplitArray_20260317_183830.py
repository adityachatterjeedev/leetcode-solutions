# Last updated: 3/17/2026, 6:38:30 PM
1class Solution:
2    def waysToSplitArray(self, nums: List[int]) -> int:
3        prefs = [0] * len(nums)
4
5        prefs[0] = nums[0]
6
7        for i in range(1, len(nums)):
8            prefs[i] = prefs[i - 1] + nums[i]
9
10        total = prefs[-1]
11        count = 0
12        for i in range(len(nums) - 1):
13            left = prefs[i]
14            if left >= total - left:
15                count += 1
16
17        return count