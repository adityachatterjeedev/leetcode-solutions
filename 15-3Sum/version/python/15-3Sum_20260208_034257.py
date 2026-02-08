# Last updated: 2/8/2026, 3:42:57 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        length = len(nums)
5        res = []
6        curr = -(10 ** 5) - 1
7        for i, num in enumerate(nums):
8
9            if num > 0:
10                break
11            if num > curr:
12                curr = num
13                left = i + 1                    
14                right = length - 1
15
16                while left < right:
17                    target = -curr
18                    l_num = nums[left]
19                    total = l_num + nums[right]
20                    if total == target:
21                        res.append([curr, l_num, nums[right]])
22                        while nums[left] == l_num and left < right:
23                            left += 1
24                    elif total < target:
25                        left += 1
26                    else:
27                        right -= 1
28                        
29        return res