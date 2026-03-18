# Last updated: 3/17/2026, 8:27:16 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3
4        if len(bloomDay) // k < m:
5            return -1
6
7        l, r = min(bloomDay), max(bloomDay)
8        res = r
9
10        while l <= r:
11            mid = (l + r) // 2
12
13            bouquet_count = 0
14            bloom_count = 0
15            for bloom in bloomDay:
16                if bloom > mid:
17                    bloom_count = 0
18                else:
19                    bloom_count += 1
20                    if bloom_count == k:
21                        bouquet_count += 1
22                        bloom_count = 0
23                    if bouquet_count == m:
24                        break
25
26            if bouquet_count >= m:
27                res = mid
28                r = mid - 1
29            else:
30                l = mid + 1
31
32        return res