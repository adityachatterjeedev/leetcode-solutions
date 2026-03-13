# Last updated: 3/13/2026, 5:35:04 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3
4        l, r = max(weights), sum(weights)
5
6        candidate = r
7
8        while l <= r:
9            mid = (l + r) // 2
10            total_days = 0
11            cum_weights = 0
12            for i, weight in enumerate(weights):
13                cum_weights += weight
14                if cum_weights > mid:
15                    total_days += 1
16                    cum_weights = weight
17            total_days += 1
18
19            if total_days > days:
20                l = mid + 1
21            else:
22                candidate = mid
23                r = mid - 1
24
25        return candidate