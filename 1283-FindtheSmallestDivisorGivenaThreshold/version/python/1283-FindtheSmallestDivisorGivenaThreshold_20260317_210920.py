# Last updated: 3/17/2026, 9:09:20 PM
1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3
4        ma = max(nums)
5
6        if threshold == len(nums):
7            return ma
8
9        l, r = 1, ma
10
11        while l <= r:
12            mid = (l + r) // 2
13
14            val = 0
15            for num in nums:
16                val += (num // mid) + (num % mid != 0)
17
18            if val <= threshold:
19                r = mid - 1
20            else:
21                l = mid + 1
22
23        return l