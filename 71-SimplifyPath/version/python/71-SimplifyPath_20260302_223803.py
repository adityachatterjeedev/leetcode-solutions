# Last updated: 3/2/2026, 10:38:03 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        lst = path.split('/')
4        stack = []
5
6        for s in lst:
7            if s:
8                if s == '.':
9                    continue
10                elif s == '..':
11                    if stack:
12                        stack.pop()
13                else:
14                    stack.append(s)
15
16        return '/' + '/'.join(stack)  