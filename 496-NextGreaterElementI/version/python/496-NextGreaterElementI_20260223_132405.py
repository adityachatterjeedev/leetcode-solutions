# Last updated: 2/23/2026, 1:24:05 PM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        ans = [-1] * len(nums1)
4
5        #stage 1: find next greates elements:
6        ng = {}
7        stack = []
8        for num in nums2:
9            while stack and stack[-1] < num:
10                top = stack.pop()
11                ng[top] = num
12            stack.append(num)
13
14        #stage 2
15        for i, n in enumerate(nums1):
16            if n in ng:
17                ans[i] = ng[n]
18
19
20        return ans