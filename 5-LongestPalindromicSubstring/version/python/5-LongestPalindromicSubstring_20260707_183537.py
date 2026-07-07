# Last updated: 7/7/2026, 6:35:37 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if len(s) == 1:
4            return s
5        
6        t = '^#' + '#'.join(s) + '#!'
7
8        C = 0
9        R = 0
10        P = [0] * len(t)
11
12        for i in range(1, len(t) - 1):
13            mirror = 2 * C - i
14
15            if i < R:
16                P[i] = min(R - i, P[mirror])
17
18            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
19                P[i] += 1
20
21            if i + P[i] > R:
22                C = i
23                R = i + P[i]
24
25        #recover
26        max_len = 0
27        center = 0
28
29        for i in range(0, len(P)-1):
30            if P[i] > max_len:
31                max_len = P[i]
32                center = i
33
34        start = (center - max_len) // 2
35        return s[start : start + max_len]
36        