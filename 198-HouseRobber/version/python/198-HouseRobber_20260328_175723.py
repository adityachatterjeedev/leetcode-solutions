# Last updated: 3/28/2026, 5:57:23 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5        dp_table = [0] * len(nums)
6        dp_table[0] = nums[0]
7        dp_table[1] = max(nums[0], nums[1])
8        for i in range(2, len(nums)):
9            dp_table[i] = max(nums[i] + dp_table[i - 2], dp_table[i - 1])
10
11        return dp_table[-1]