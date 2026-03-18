# Last updated: 3/17/2026, 8:01:00 PM
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
15            for i, pos in enumerate(position):
16                if i == 0:
17                    continue
18                if pos - curr >= mid:
19                    curr = pos
20                    ball_count += 1
21                    if ball_count == m:
22                        break
23
24
25            if ball_count >= m:
26                l = mid + 1
27            else:
28                r = mid - 1
29
30        return r