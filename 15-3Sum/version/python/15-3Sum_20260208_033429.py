# Last updated: 2/8/2026, 3:34:29 AM
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
18                    l_num = nums[left]
19                    r_num = nums[right]
20                    total = l_num + r_num + curr
21                    if total == 0:
22                        res.append([curr, l_num, r_num])
23                        while nums[left] == l_num and left < right:
24                            left += 1
25                        while nums[right] == r_num and left < right:
26                            right -= 1
27                    elif total < 0:
28                        left += 1
29                    else:
30                        right -= 1
31                        
32
33        return res