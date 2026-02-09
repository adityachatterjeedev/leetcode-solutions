# Last updated: 2/8/2026, 10:28:26 PM
1class Solution:
2    def maxArea(self, heights: List[int]) -> int:
3        res = 0
4        left, right = 0, len(heights) - 1
5        while left < right:
6            l_height, r_height = heights[left], heights[right]
7            vol = (right - left) * (l_height if l_height < r_height else r_height)
8            res = res if vol <= res else vol
9            if l_height < r_height:
10                left += 1
11            else:
12                right -= 1
13
14        return res