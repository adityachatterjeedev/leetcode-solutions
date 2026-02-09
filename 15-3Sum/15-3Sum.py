# Last updated: 2/8/2026, 10:04:34 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        res = []
5
6        for i in range(len(nums) - 2):
7            if nums[i] > 0:
8                break
9            
10            num = nums[i]
11            if i > 0 and nums[i] == nums[i - 1]:
12                continue
13            if num + nums[i + 1] + nums[i + 2] > 0:
14                break
15            if num + nums[-1] + nums[-2] < 0:
16                continue
17            
18            left = i + 1                    
19            right = len(nums) - 1
20
21            while left < right:
22                target = -num
23                total = nums[left] + nums[right]
24                if total == target:
25                    l_num, r_num = nums[left], nums[right]
26                    res += [[num, l_num, r_num]]
27                    while nums[left] == l_num and left < right:
28                        left += 1
29                    while nums[right] == r_num and left < right:
30                        right -= 1
31                elif total < target:
32                    l_num = nums[left]
33                    while nums[left] == l_num and left < right:
34                        left += 1
35                else:
36                    r_num = nums[right]
37                    while nums[right] == r_num and left < right:
38                        right -= 1
39                        
40        return res