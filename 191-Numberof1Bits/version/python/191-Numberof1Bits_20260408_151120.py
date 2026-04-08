# Last updated: 4/8/2026, 3:11:20 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        res = 0
4        while n:
5            res += (n & 1)
6            n = n >> 1
7        return res
8        
9