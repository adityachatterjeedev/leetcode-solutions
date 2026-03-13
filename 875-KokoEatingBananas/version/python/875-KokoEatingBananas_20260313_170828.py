# Last updated: 3/13/2026, 5:08:28 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 0
        right = max(piles)
        while left + 1 < right:
            midd = (left + right) // 2
            total_hours = 0
            for p in piles:
                total_hours += (p-1) // midd + 1
            if total_hours <= h:
                right = midd
            else:
                left = midd
        return right