# Last updated: 3/17/2026, 6:06:50 PM
1class Solution:
2    def splitArray(self, nums: List[int], k: int) -> int:
3        
4        l, r = max(nums), sum(nums)
5
6        res = r
7
8        while l <= r:
9            mid = (l + r) // 2
10
11            arr_count = 1
12
13            curr_sum = 0
14
15            for num in nums:
16                curr_sum += num
17                if curr_sum > mid:
18                    arr_count += 1
19                    curr_sum = num
20            
21            if arr_count <= k:
22                res = mid
23                r = mid - 1
24            else:
25                l = mid + 1
26
27        return res