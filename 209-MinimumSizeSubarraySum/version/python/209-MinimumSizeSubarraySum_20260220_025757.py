# Last updated: 2/20/2026, 2:57:57 AM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        res = 100001
4        max_right = len(nums) - 1
5        if nums[0] >= target:
6            return 1
7        window_sum = 0
8        window_len = 0
9        left = 0
10
11        for right, num in enumerate(nums):
12            window_sum += num
13            window_len += 1
14
15            while window_sum >= target:
16                if window_len < res:
17                    res = window_len
18                window_sum -= nums[left]
19                window_len -= 1
20                left += 1
21
22        if res < 100001:
23            return res
24        else:
25            return 0