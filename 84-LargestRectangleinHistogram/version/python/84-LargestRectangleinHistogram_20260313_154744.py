# Last updated: 3/13/2026, 3:47:44 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4
5        le = len(heights)
6
7        max_area = 0
8
9        for i,height in enumerate(heights):
10            start = i
11            while stack and stack[-1][1] >= height:
12                ind, ht = stack.pop()
13                max_area = max(max_area, ht * (i - ind))
14                start = ind
15
16            stack.append((start, height))
17        
18        for st,ht in stack:
19            max_area = max(max_area, ht * (le - st))
20
21        return max_area