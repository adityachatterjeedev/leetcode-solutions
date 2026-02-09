# Last updated: 2/8/2026, 10:02:27 PM
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
25                    l_num = nums[left]
26                    res += [[num, l_num, nums[right]]]
27                    while nums[left] == l_num and left < right:
28                        left += 1
29                elif total < target:
30                    left += 1
31                else:
32                    right -= 1
33                        
34        return res