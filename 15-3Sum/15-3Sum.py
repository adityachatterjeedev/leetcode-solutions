# Last updated: 2/8/2026, 3:51:46 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        res = []
5
6        for i, num in enumerate(nums):
7            if num > 0:
8                break
9            if i == 0 or num != nums[i - 1]:
10                left = i + 1                    
11                right = len(nums) - 1
12
13                while left < right:
14                    target = -num
15                    total = nums[left] + nums[right]
16                    if total == target:
17                        l_num = nums[left]
18                        res.append([num, l_num, nums[right]])
19                        while nums[left] == l_num and left < right:
20                            left += 1
21                    elif total < target:
22                        left += 1
23                    else:
24                        right -= 1
25                        
26        return res