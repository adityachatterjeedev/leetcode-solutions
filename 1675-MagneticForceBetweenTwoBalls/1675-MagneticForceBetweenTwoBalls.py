# Last updated: 7/7/2026, 6:35:55 PM
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        l, r = 1, position[-1] - position[0]

        n = len(position)

        while l <= r:
            mid = (l + r) // 2

            ball_count = 1
            curr = position[0]

            for i in range(1, n):
                if position[i] - curr >= mid:
                    curr = position[i]
                    ball_count += 1
                    if ball_count == m:
                        break


            if ball_count >= m:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return r