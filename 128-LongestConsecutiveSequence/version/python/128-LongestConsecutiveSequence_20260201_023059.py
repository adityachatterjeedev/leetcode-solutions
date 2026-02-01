# Last updated: 2/1/2026, 2:30:59 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        contents = set(nums)
6        max_len = 1
7        for num in contents:
8            if (num - 1) not in contents:
9                seq_len = 1
10                curr = num
11                while (curr + 1) in contents:
12                    seq_len += 1
13                    curr = curr + 1
14
15                max_len = max(max_len, seq_len)
16
17        return max_len