# Last updated: 2/1/2026, 2:06:30 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        numSet = set(nums)
6        longest = 0
7
8        for num in numSet:
9            if (num - 1) not in numSet:
10                length = 1
11                while (num + length) in numSet:
12                    length += 1
13                longest = max(length, longest)
14        return longest