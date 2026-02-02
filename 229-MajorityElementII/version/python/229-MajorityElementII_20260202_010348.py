# Last updated: 2/2/2026, 1:03:48 AM
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
11        c1 = nums[0]
12        count1 = 1
13        pos = 1
14        while nums[pos] == c1:
15            pos += 1
16            count1 += 1
17            if pos == len(nums):
18                return [c1]
19        c2 = nums[pos]
20        count2 = 1
21
22        for i in range(pos + 1, len(nums)):
23            if nums[i] == c1:
24                count1 += 1
25            elif nums[i] == c2:
26                count2 += 1
27            elif count1 == 0:
28                c1 = nums[i]
29                count1 = 1
30            elif count2 == 0:
31                c2 = nums[i]
32                count2 = 1
33            else:
34                count1 -= 1
35                count2 -= 1
36
37        #check
38        count1, count2 = 0, 0
39        for num in nums:
40            if num == c1:
41                count1 += 1
42            elif num == c2:
43                count2 += 1
44
45        threshold = int(len(nums) / 3)
46        res = []
47        if count1 > threshold:
48            res.append(c1)
49        if count2 > threshold:
50            res.append(c2)
51        return res