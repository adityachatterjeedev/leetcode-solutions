# Last updated: 2/21/2026, 12:33:33 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3
4        if len(t) > len(s):
5            return ''
6        ct = Counter(t)
7        res = [0, len(s)]
8        reslen = float('inf')
9        t_char_count = len(ct) # no. of unique chars in t
10
11        window_chars = Counter()
12        left = 0
13        have_count = 0 # number of matches
14
15        for right, char in enumerate(s):
16            if char in ct:
17                window_chars[char] += 1
18                if window_chars[char] == ct[char]:
19                    have_count += 1
20
21                while have_count == t_char_count:
22                    if (right - left + 1) < reslen:
23                        res = [left, right + 1]
24                        reslen = right - left + 1
25                    
26                    if s[left] in ct:
27                        l_char = s[left]
28                        window_chars[l_char] -= 1
29                        if window_chars[l_char] < ct[l_char]:
30                            have_count -= 1
31                    left += 1
32        
33        return '' if reslen == float('inf') else s[res[0]: res[1]]