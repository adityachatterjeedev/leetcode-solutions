# Last updated: 3/17/2026, 9:11:22 PM
1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3
4        ma = max(nums)
5
6        if threshold == len(nums):
7            return ma
8        
9        if threshold >= sum(nums):
10            return 1
11
12        l, r = 2, ma - 1
13
14        while l <= r:
15            mid = (l + r) // 2
16
17            val = 0
18            for num in nums:
19                val += (num // mid) + (num % mid != 0)
20
21            if val <= threshold:
22                r = mid - 1
23            else:
24                l = mid + 1
25
26        return l