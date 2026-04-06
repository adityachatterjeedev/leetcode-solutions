# Last updated: 4/5/2026, 8:55:11 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        res = 0
4        for num in nums:
5            res ^= num
6
7        return res    