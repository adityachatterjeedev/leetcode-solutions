# Last updated: 2/7/2026, 9:21:44 PM
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
15            val -= 1
16            if nums[val] > 0:
17                nums[val] *= -1
18
19        for i in range(n):
20            if nums[i] >= 0:
21                return i + 1
22
23        return n + 1