# Last updated: 2/19/2026, 3:14:45 AM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        ones_count = 0
4        max_ones = 0
5        left = 0
6        window_size = 0
7        res = 0
8        for right in range(len(nums)):
9            digit = nums[right]
10            window_size += 1
11            if digit == 1:
12                ones_count += 1
13            if ones_count > max_ones:
14                max_ones = ones_count
15            while (window_size - max_ones) > k:
16                if nums[left] == 1:
17                    ones_count -= 1
18                left += 1
19                window_size -= 1
20
21            if window_size > res:
22                res = window_size
23        
24        return res
25            
26            