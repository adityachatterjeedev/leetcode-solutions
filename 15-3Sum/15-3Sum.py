# Last updated: 2/8/2026, 10:01:04 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:        
3        nums.sort()
4        res = []
5
6        for i in range(len(nums) - 2):
7            if nums[i] > 0:
8                break
9            num = nums[i]
10            if num + nums[i + 1] + nums[i + 2] > 0:
11                break
12            if num + nums[-1] + nums[-2] < 0:
13                continue
14            if i == 0 or num != nums[i - 1]:
15                left = i + 1                    
16                right = len(nums) - 1
17
18                while left < right:
19                    target = -num
20                    total = nums[left] + nums[right]
21                    if total == target:
22                        l_num = nums[left]
23                        res += [[num, l_num, nums[right]]]
24                        while nums[left] == l_num and left < right:
25                            left += 1
26                    elif total < target:
27                        left += 1
28                    else:
29                        right -= 1
30                        
31        return res