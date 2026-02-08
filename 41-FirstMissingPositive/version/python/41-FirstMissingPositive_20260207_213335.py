# Last updated: 2/7/2026, 9:33:35 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        
4        n = len(nums)
5
6        for i in range(n):
7            if nums[i] <= 0:
8                nums[i] = n + 1
9
10        for i in range(n):
11            val = nums[i]
12            if val < 0:
13                val = -val
14            if val > n:
15                continue
16            
17            val -= 1
18            if nums[val] > 0:
19                nums[val] *= -1
20
21        for i in range(n):
22            if nums[i] >= 0:
23                return i + 1
24
25        return n + 1