# Last updated: 2/20/2026, 2:56:09 AM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        res = 100001
4        max_right = len(nums) - 1
5        if nums[0] >= target:
6            return 1
7        window_sum = nums[0]
8        window_len = 1
9        left, right = 0, 0
10
11        while right < max_right:
12            right += 1
13            window_sum += nums[right]
14            window_len += 1
15
16            while window_sum >= target:
17                if window_len < res:
18                    res = window_len
19                window_sum -= nums[left]
20                window_len -= 1
21                left += 1
22
23        if res < 100001:
24            return res
25        else:
26            return 0