# Last updated: 2/8/2026, 3:30:07 AM
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
20                    l_flag, r_flag = False, False
21                    total = l_num + r_num
22                    if total == target:
23                        res.append([curr, l_num, r_num])
24                        l_flag, r_flag = True, True
25                    elif total < target:
26                        l_flag = True
27                    else:
28                        r_flag = True
29                    
30                    # update left and right pointers
31                    if l_flag:
32                        while nums[left] == l_num and left < right:
33                            left += 1
34                    if r_flag:
35                        while nums[right] == r_num and left < right:
36                            right -= 1
37
38        return res