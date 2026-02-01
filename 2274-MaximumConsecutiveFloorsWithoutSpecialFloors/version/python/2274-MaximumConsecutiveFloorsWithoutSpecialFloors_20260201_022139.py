# Last updated: 2/1/2026, 2:21:39 AM
1class Solution:
2    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
3        max_consec = 0
4        special.sort()
5        for i in range(len(special) -1):
6            max_consec = max(max_consec, special[i + 1] - special[i] - 1)
7
8        return max(max_consec, special[0] - bottom, top - special[-1])