# Last updated: 2/8/2026, 3:32:54 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        length = len(nums)
5        res = []
6        curr = -(10 ** 5) - 1
7        for i in range(length - 2):
8            num  = nums[i]
9            if num > 0:
10                break
11            if num > curr:
12                curr = num
13                left = i + 1                    
14                right = length - 1
15
16                # main while loop for two-sum
17                while left < right:
18                    target = -curr
19                    l_num = nums[left]
20                    r_num = nums[right]
21                    total = l_num + r_num
22                    if total == target:
23                        res.append([curr, l_num, r_num])
24                        while nums[left] == l_num and left < right:
25                            left += 1
26                        while nums[right] == r_num and left < right:
27                            right -= 1
28                    elif total < target:
29                        left += 1
30                    else:
31                        right -= 1
32                        
33
34        return res