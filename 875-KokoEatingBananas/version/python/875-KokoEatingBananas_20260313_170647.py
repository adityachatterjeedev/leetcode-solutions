# Last updated: 3/13/2026, 5:06:47 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        piles.sort()
4
5        l, r = 1, piles[-1]
6        candidate = 0
7        while l <= r:
8            mid = (l + r) // 2
9            total = 0
10            for pile in piles:
11                total += math.ceil(pile / mid)
12            if total > h:
13                l = mid + 1
14            else:
15                candidate = mid
16                r = mid - 1
17
18        return candidate