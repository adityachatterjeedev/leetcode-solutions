# Last updated: 4/5/2026, 9:15:34 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        return (bin(n)).count('1')