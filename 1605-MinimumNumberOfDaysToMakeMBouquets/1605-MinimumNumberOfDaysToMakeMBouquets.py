# Last updated: 7/7/2026, 6:35:56 PM
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) // k < m:
            return -1

        l, r = min(bloomDay), max(bloomDay)

        while l <= r:
            mid = (l + r) // 2

            bouquet_count = 0
            bloom_count = 0
            for bloom in bloomDay:
                if bloom > mid:
                    bloom_count = 0
                else:
                    bloom_count += 1
                    bouquet_count += bloom_count // k
                    bloom_count %= k

            if bouquet_count >= m:
                r = mid - 1
            else:
                l = mid + 1

        return l