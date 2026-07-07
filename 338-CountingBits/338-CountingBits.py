# Last updated: 7/7/2026, 6:36:31 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]