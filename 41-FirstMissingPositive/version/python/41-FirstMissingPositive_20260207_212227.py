# Last updated: 2/7/2026, 9:22:27 PM
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
11            val = abs(nums[i])
12            if val > n:
13                continue
14            
15            if nums[val - 1] > 0:
16                nums[val - 1] *= -1
17
18        for i in range(n):
19            if nums[i] >= 0:
20                return i + 1
21
22        return n + 1