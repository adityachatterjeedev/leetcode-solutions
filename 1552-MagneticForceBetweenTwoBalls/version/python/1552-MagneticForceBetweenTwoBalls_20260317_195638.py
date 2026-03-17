# Last updated: 3/17/2026, 7:56:38 PM
1class Solution:
2    def maxDistance(self, position: List[int], m: int) -> int:
3        position.sort()
4
5        l, r = 1, position[-1] - position[0]
6
7        res = 1
8        while l <= r:
9            mid = (l + r) // 2
10
11            ball_count = 1
12            curr = position[0]
13
14            for i in range(1, len(position)):
15                if position[i] - curr >= mid:
16                    curr = position[i]
17                    ball_count += 1
18                    if ball_count == m:
19                        break
20
21
22            if ball_count >= m:
23                res = mid
24                l = mid + 1
25            else:
26                r = mid - 1
27
28        return res