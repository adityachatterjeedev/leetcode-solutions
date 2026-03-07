# Last updated: 3/7/2026, 3:45:20 AM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        string_stack = []
4        count_stack = []
5
6        curr = ""
7        k = 0
8
9        for c in s:
10            if c.isdigit():
11                k = (10 * k) + int(c)
12            elif c == '[':
13                string_stack.append(curr)
14                count_stack.append(k)
15                curr = ''
16                k = 0
17            elif c == ']':
18                curr = (count_stack.pop()) * curr
19                curr = string_stack.pop() + curr
20            else:
21                curr += c
22
23        return curr