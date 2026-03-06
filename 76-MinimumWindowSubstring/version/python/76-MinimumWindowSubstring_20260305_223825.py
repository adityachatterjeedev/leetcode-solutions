# Last updated: 3/5/2026, 10:38:25 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if len(t) > len(s):
4            return ""
5
6        res = [-1,-1]
7        reslen = float('inf')
8
9        t_counts = {}
10        for c in t:
11            t_counts[c] = 1 + t_counts.get(c, 0)
12        
13        num_t_unique_chars = len(t_counts)
14        
15        le_s, le_t = len(s), len(t)
16
17        left = 0
18        window_counts = {}
19
20        have = 0
21
22        for right, r_char in enumerate(s):
23            if r_char in t_counts:
24                window_counts[r_char] = 1 + window_counts.get(r_char, 0)
25                if window_counts[r_char] == t_counts[r_char]:
26                    have += 1
27
28                while have == num_t_unique_chars:
29                    if right - left + 1 < reslen:
30                        res = [left, right]
31                        reslen = right - left + 1
32                    
33                    if s[left] in t_counts:
34                        l_char = s[left]
35                        window_counts[l_char] -= 1
36                        if window_counts[l_char] == t_counts[l_char] - 1:
37                            have -= 1
38                    left += 1
39
40        return '' if reslen == float('inf') else s[res[0]: res[1] + 1]