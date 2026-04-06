# Last updated: 4/5/2026, 9:15:57 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        num = n
4        res = 0
5        while num:
6            res += num % 2
7            num = num >> 1
8        return res