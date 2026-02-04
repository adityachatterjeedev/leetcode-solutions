# Last updated: 2/3/2026, 10:47:44 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        n = len(nums)
4        #three loops
5        for i in range(n):
6            if nums[i] <= 0 or nums[i] > n:
7                nums[i] = n + 1
8
9        for i in range(n):
10            num = abs(nums[i])
11
12            if num > n:
13                continue
14            
15            if nums[num - 1] > 0:
16                nums[num - 1] *= -1
17
18        for i in range(n):
19            if nums[i] > 0:
20                return i + 1
21
22        return n + 1