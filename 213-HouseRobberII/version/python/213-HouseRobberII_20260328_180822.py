# Last updated: 3/28/2026, 6:08:22 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        le = len(nums)
4        if le == 1:
5            return nums[0]
6        elif le == 2:
7            return max(nums[0], nums[1])
8        
9        def dp(flag: bool):
10            dp_table = [0] * (le - 1)
11
12            start = 0
13            if flag:
14                start += 1
15            dp_table[0] = nums[start]
16            dp_table[1] = max(nums[start], nums[start + 1])
17            for i in range(2, le - 1):
18                dp_table[i] = max(nums[start + i] + dp_table[i - 2], dp_table[i - 1])
19            return dp_table[-1]
20        
21        return max(dp(False), dp(True))