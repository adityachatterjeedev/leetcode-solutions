# Last updated: 2/8/2026, 3:44:05 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        res = []
5        curr = -(10 ** 5) - 1
6        for i, num in enumerate(nums):
7            if num > 0:
8                break
9            if num > curr:
10                curr = num
11                left = i + 1                    
12                right = len(nums) - 1
13
14                while left < right:
15                    target = -curr
16                    l_num = nums[left]
17                    total = l_num + nums[right]
18                    if total == target:
19                        res.append([curr, l_num, nums[right]])
20                        while nums[left] == l_num and left < right:
21                            left += 1
22                    elif total < target:
23                        left += 1
24                    else:
25                        right -= 1
26                        
27        return res