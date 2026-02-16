# Last updated: 2/16/2026, 5:30:21 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        if not height:
4            return 0
5
6        left ,right = 0, len(height) - 1
7        res = 0
8        l_max, r_max = height[0], height[-1]
9
10        while left < right:
11            if l_max < r_max:
12                left += 1
13                l_max = max(l_max, height[left])
14                res += l_max - height[left]
15            else:
16                right -= 1
17                r_max = max(r_max, height[right])
18                res += r_max - height[right]
19        
20        return res