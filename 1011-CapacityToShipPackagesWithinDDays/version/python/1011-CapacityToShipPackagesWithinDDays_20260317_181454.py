# Last updated: 3/17/2026, 6:14:54 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        
4        if days == 1:
5            return sum(weights)
6
7        l, r = max(weights), sum(weights)
8
9        res = r
10        while l <= r:
11            mid = (l + r) // 2
12
13            day_count = 1
14            weight_sum = 0
15            for weight in weights: 
16                weight_sum += weight
17                if weight_sum > mid:
18                    day_count += 1
19                    weight_sum = weight
20
21                
22            if day_count > days:
23                l = mid + 1
24            else:
25                res = mid
26                r = mid - 1
27            
28        return res