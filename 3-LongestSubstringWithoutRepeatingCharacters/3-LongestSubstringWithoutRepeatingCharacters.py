# Last updated: 2/11/2026, 4:55:17 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        if not s:
4            return 0
5        length = len(s)
6        max_len = 1
7        contents = set(s[0])
8        left, right = 0, 0
9        curr = 1
10
11        while right < length - 1:
12            nxt = s[right + 1]
13            if nxt not in contents:
14                right += 1
15                curr += 1
16                contents.add(nxt)
17                if right == length - 1:
18                    return curr if curr > max_len else max_len
19            else:
20                max_len = curr if curr > max_len else max_len
21                while s[left] != nxt:
22                    contents.remove(s[left])
23                    left += 1
24                left += 1
25                right += 1
26                curr = right - left + 1
27
28        return max_len
29