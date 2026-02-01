# Last updated: 2/1/2026, 2:11:02 AM
1class Solution:
2    def sumOfThree(self, num: int) -> List[int]:
3        if num % 3 != 0:
4            return []
5
6        quot = num // 3
7
8        return [quot -1, quot, quot + 1]