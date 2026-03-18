# Last updated: 3/17/2026, 8:01:47 PM
1class Solution:
2    def maxDistance(self, position: List[int], m: int) -> int:
3        position.sort()
4
5        l, r = 1, position[-1] - position[0]
6
7        n = len(position)
8
9        while l <= r:
10            mid = (l + r) // 2
11
12            ball_count = 1
13            curr = position[0]
14
15            for i in range(1, n):
16                if position[i] - curr >= mid:
17                    curr = position[i]
18                    ball_count += 1
19                    if ball_count == m:
20                        break
21
22
23            if ball_count >= m:
24                res = mid
25                l = mid + 1
26            else:
27                r = mid - 1
28
29        return r