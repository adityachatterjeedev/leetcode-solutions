# Last updated: 2/27/2026, 8:55:29 AM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        if k == len(num):
4            return "0"
5        
6        lst = list(num)
7        
8        stack = []
9
10        for c in lst:
11            while k > 0 and stack and stack[-1] > c:
12                stack.pop()
13                k -= 1
14
15            stack.append(c)
16        
17        stack = stack[:len(stack) - k]
18
19        res = "".join(stack).lstrip('0')
20        return res if res else "0"