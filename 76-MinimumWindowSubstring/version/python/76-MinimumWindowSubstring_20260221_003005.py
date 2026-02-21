# Last updated: 2/21/2026, 12:30:05 AM
1from collections import Counter #used to quickly check if there exists a valid solution
2class Solution:
3    def minWindow(self, s: str, t: str) -> str:
4        cs, ct = Counter(s), Counter(t)
5
6        if not ct <= cs: # if no valid solution
7            return ""
8        res = [0, len(s)]
9        reslen = len(s)
10        t_char_count = len(ct) # no. of unique chars in t
11
12        window_chars = Counter()
13        left = 0
14        have_count = 0 # number of matches
15
16        for right, char in enumerate(s):
17            if char in ct:
18                window_chars[char] += 1
19                if window_chars[char] == ct[char]:
20                    have_count += 1
21
22                while have_count == t_char_count:
23                    if (right - left + 1) < reslen:
24                        res = [left, right + 1]
25                        reslen = right - left + 1
26                    
27                    if s[left] in ct:
28                        l_char = s[left]
29                        window_chars[l_char] -= 1
30                        if window_chars[l_char] < ct[l_char]:
31                            have_count -= 1
32                    left += 1
33        
34        return s[res[0]: res[1]]