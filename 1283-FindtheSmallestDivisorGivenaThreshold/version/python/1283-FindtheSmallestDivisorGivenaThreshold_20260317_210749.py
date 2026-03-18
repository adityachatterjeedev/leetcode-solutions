# Last updated: 3/17/2026, 9:07:49 PM
1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3        le = len(nums)
4
5        ma = max(nums)
6
7        if threshold == le:
8            return ma
9
10        l, r = 1, ma
11
12        while l <= r:
13            mid = (l + r) // 2
14
15            val = 0
16            for num in nums:
17                val += (num // mid) + (num % mid != 0)
18                if val > threshold:
19                    break
20
21            if val <= threshold:
22                r = mid - 1
23            else:
24                l = mid + 1
25
26        return l
27