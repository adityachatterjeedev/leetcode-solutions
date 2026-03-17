# Last updated: 3/17/2026, 6:13:06 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        
4        l, r = max(weights), sum(weights)
5
6        res = r
7        while l <= r:
8            mid = (l + r) // 2
9
10            day_count = 1
11            weight_sum = 0
12            for weight in weights: 
13                weight_sum += weight
14                if weight_sum > mid:
15                    day_count += 1
16                    weight_sum = weight
17
18                
19            if day_count > days:
20                l = mid + 1
21            else:
22                res = mid
23                r = mid - 1
24            
25        return res