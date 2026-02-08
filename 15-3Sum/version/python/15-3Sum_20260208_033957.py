# Last updated: 2/8/2026, 3:39:57 AM
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
19                    total = l_num + nums[right] + curr
20                    if total == 0:
21                        res.append([curr, l_num, nums[right]])
22                        while nums[left] == l_num and left < right:
23                            left += 1
24                    elif total < 0:
25                        left += 1
26                    else:
27                        right -= 1
28                        
29
30        return res