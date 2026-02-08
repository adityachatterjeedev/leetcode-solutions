# Last updated: 2/8/2026, 3:31:46 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        length = len(nums)
5        res = []
6        curr = -(10 ** 5) - 1
7        for i in range(length - 2):
8            if nums[i] > 0:
9                break
10            if nums[i] > curr:
11                curr = nums[i]
12                left = i + 1                    
13                right = length - 1
14
15                # main while loop for two-sum
16                while left < right:
17                    target = -curr
18                    l_num = nums[left]
19                    r_num = nums[right]
20                    total = l_num + r_num
21                    if total == target:
22                        res.append([curr, l_num, r_num])
23                        while nums[left] == l_num and left < right:
24                            left += 1
25                        while nums[right] == r_num and left < right:
26                            right -= 1
27                    elif total < target:
28                        left += 1
29                    else:
30                        right -= 1
31                        
32
33        return res