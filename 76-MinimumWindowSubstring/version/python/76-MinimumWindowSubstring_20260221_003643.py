# Last updated: 2/21/2026, 12:36:43 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3
4        if len(t) > len(s):
5            return ''
6        
7        ct = {}
8        for c in t:
9            ct[c] = 1 + ct.get(c, 0)
10
11        res = [0, len(s)]
12        reslen = float('inf')
13        t_char_count = len(ct) # no. of unique chars in t
14
15        window_chars = {}
16        left = 0
17        have_count = 0 # number of matches
18
19        for right, char in enumerate(s):
20            if char in ct:
21                window_chars[char] = 1 + window_chars.get(char, 0)
22                if window_chars[char] == ct[char]:
23                    have_count += 1
24
25                while have_count == t_char_count:
26                    if (right - left + 1) < reslen:
27                        res = [left, right + 1]
28                        reslen = right - left + 1
29                    
30                    if s[left] in ct:
31                        l_char = s[left]
32                        window_chars[l_char] -= 1
33                        if window_chars[l_char] < ct[l_char]:
34                            have_count -= 1
35                    left += 1
36        
37        return '' if reslen == float('inf') else s[res[0]: res[1]]