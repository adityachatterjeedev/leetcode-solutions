# Last updated: 3/2/2026, 9:50:12 PM
1class Solution:
2    def nextGreaterElements(self, nums: List[int]) -> List[int]:
3        stack = []
4
5        res = [-1] * len(nums)
6
7        for i, num in enumerate(nums):
8            while stack and stack[-1][0] < num:
9                res[stack.pop()[1]] = num
10            stack.append((num, i))
11
12        for num in nums:
13            while stack and stack[-1][0] < num:
14                res[stack.pop()[1]] = num
15
16        return res