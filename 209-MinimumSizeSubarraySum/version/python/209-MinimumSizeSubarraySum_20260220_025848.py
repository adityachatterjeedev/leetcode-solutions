# Last updated: 2/20/2026, 2:58:48 AM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        res = 100001
4        max_right = len(nums) - 1
5        if nums[0] >= target:
6            return 1
7        window_sum = 0
8        left = 0
9
10        for right, num in enumerate(nums):
11            window_sum += num
12
13            while window_sum >= target:
14                res = min(res, right - left + 1)
15                window_sum -= nums[left]
16                left += 1
17
18        if res < 100001:
19            return res
20        else:
21            return 0