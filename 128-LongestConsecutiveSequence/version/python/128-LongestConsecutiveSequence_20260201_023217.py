# Last updated: 2/1/2026, 2:32:17 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        contents = set(nums)
6        max_len = 1
7        for num in contents:
8            if (num - 1) not in contents:
9                length = 1
10                while (num + length) in contents:
11                    length += 1
12
13                max_len = max(max_len, length)
14
15        return max_len