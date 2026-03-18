# Last updated: 3/17/2026, 8:23:28 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3        le = len(bloomDay)
4
5        if le // k < m:
6            return -1
7
8        l, r = 1, max(bloomDay)
9        res = r
10
11        while l <= r:
12            mid = (l + r) // 2
13
14            bouquet_count = 0
15            bloom_count = 0
16            for bloom in bloomDay:
17                if bloom > mid:
18                    bloom_count = 0
19                else:
20                    bloom_count += 1
21                    if bloom_count == k:
22                        bouquet_count += 1
23                        bloom_count = 0
24                    if bouquet_count == m:
25                        break
26
27            if bouquet_count >= m:
28                res = mid
29                r = mid - 1
30            else:
31                l = mid + 1
32
33        return res