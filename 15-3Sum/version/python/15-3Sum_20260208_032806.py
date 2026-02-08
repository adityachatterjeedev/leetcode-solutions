# Last updated: 2/8/2026, 3:28:06 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        length = len(nums)
5        res = []
6        curr = -(10 ** 5) - 1
7        for i in range(length - 2):
8            if nums[i] > curr:
9                curr = nums[i]
10                left = i + 1                    
11                right = length - 1
12
13                # main while loop for two-sum
14                while left < right:
15                    target = -curr
16                    l_num = nums[left]
17                    r_num = nums[right]
18                    l_flag, r_flag = False, False
19                    total = l_num + r_num
20                    if total == target:
21                        res.append([curr, l_num, r_num])
22                        l_flag, r_flag = True, True
23                    elif total < target:
24                        l_flag = True
25                    else:
26                        r_flag = True
27                    
28                    # update left and right pointers
29                    if l_flag:
30                        while nums[left] == l_num and left < right:
31                            left += 1
32                    if r_flag:
33                        while nums[right] == r_num and left < right:
34                            right -= 1
35
36        return res