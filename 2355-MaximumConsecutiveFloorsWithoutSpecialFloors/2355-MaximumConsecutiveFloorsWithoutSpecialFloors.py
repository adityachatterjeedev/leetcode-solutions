# Last updated: 2/8/2026, 3:49:13 AM
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        max_consec = 0
        special.sort()
        for i in range(len(special) -1):
            max_consec = max(max_consec, special[i + 1] - special[i] - 1)

        return max(max_consec, special[0] - bottom, top - special[-1])