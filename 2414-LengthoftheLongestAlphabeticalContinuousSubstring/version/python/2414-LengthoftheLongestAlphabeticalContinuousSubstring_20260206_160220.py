# Last updated: 2/6/2026, 4:02:20 PM
1class Solution:
2    def longestContinuousSubstring(self, s: str) -> int:
3        if not s:
4            return 0
5
6        max_len = 1
7        curr_len = 1
8
9        for i in range(1, len(s)):
10            if ord(s[i]) == ord(s[i - 1]) + 1:
11                curr_len += 1
12            else:
13                curr_len = 1
14
15            max_len = max(max_len, curr_len)
16
17        return max_len