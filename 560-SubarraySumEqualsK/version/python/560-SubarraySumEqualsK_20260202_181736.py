# Last updated: 2/2/2026, 6:17:36 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        sub_count = 0
4        prefs = {0:1}
5        pref = 0
6        for num in nums:
7            pref += num
8            sub_count += prefs.get((pref - k), 0)
9            prefs[pref] = 1 + prefs.get(pref, 0)
10        return sub_count