# Last updated: 4/8/2026, 3:14:16 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        return [i.bit_count() for i in range(n + 1)]