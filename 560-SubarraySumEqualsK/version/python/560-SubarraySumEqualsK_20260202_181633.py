# Last updated: 2/2/2026, 6:16:33 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        sub_count = 0
4        prefs = defaultdict(int)
5
6        pref = 0
7        prefs[0] = 1
8        for num in nums:
9            pref += num
10            sub_count += prefs.get((pref - k), 0)
11            prefs[pref] += 1
12        return sub_count