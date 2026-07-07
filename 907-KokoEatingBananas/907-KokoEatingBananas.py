# Last updated: 7/7/2026, 6:36:07 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        candidate = 0
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total > h:
                l = mid + 1
            else:
                candidate = mid
                r = mid - 1

        return candidate