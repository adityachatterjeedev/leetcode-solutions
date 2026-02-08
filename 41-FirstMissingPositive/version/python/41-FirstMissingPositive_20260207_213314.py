# Last updated: 2/7/2026, 9:33:14 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        
4        n = len(nums)
5        nums_local = nums
6
7        for i in range(n):
8            if nums_local[i] <= 0:
9                nums_local[i] = n + 1
10
11        for i in range(n):
12            val = nums_local[i]
13            if val < 0:
14                val = -val
15            if val > n:
16                continue
17            
18            val -= 1
19            if nums_local[val] > 0:
20                nums_local[val] *= -1
21
22        for i in range(n):
23            if nums_local[i] >= 0:
24                return i + 1
25
26        return n + 1