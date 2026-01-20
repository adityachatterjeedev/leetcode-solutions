# Last updated: 1/20/2026, 4:37:20 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        res = defaultdict(list)
4        for s in strs:
5            counts = [0] * 26
6            for c in s:
7                counts[ord(c) - ord('a')] += 1
8            res[tuple(counts)].append(s)
9
10        return list(res.values())