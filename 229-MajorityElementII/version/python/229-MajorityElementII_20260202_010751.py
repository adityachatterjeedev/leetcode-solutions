# Last updated: 2/2/2026, 1:07:51 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        if len(nums) in [0,1]:
4            return nums
5        if len(nums) == 2:
6            if nums[0] == nums[1]:
7                return [nums[0]]
8            else:
9                return nums
10        
11        c1, c2 = None, None
12        count1, count2 = 0, 0
13
14        for num in nums:
15            if num == c1:
16                count1 += 1
17            elif num == c2:
18                count2 += 1
19            elif count1 == 0:
20                c1 = num
21                count1 = 1
22            elif count2 == 0:
23                c2 = num
24                count2 = 1
25            else:
26                count1 -= 1
27                count2 -= 1
28
29        #check
30        count1 = nums.count(c1)
31        count2 = nums.count(c2)
32
33        threshold = int(len(nums) / 3)
34        res = []
35        if count1 > threshold:
36            res.append(c1)
37        if count2 > threshold:
38            res.append(c2)
39        return res