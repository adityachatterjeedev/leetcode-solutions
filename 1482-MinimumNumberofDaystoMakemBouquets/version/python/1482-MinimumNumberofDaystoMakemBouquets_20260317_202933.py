# Last updated: 3/17/2026, 8:29:33 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3
4        if len(bloomDay) // k < m:
5            return -1
6
7        l, r = min(bloomDay), max(bloomDay)
8
9        while l <= r:
10            mid = (l + r) // 2
11
12            bouquet_count = 0
13            bloom_count = 0
14            for bloom in bloomDay:
15                if bloom > mid:
16                    bloom_count = 0
17                else:
18                    bloom_count += 1
19                    bouquet_count += bloom_count // k
20                    bloom_count %= k
21
22            if bouquet_count >= m:
23                r = mid - 1
24            else:
25                l = mid + 1
26
27        return l