# Last updated: 3/17/2026, 9:06:12 PM
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
17                val += math.ceil(num / mid)
18
19            if val <= threshold:
20                r = mid - 1
21            else:
22                l = mid + 1
23
24        return l
25