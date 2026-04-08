# Last updated: 4/8/2026, 3:39:03 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        if len(a) < len(b):
4            a,b = b,a
5        b = (len(a) - len(b)) * '0' + b
6        res = ['0'] * len(a)
7        s,c = 0,0
8        for i in range(len(a)-1, -1, -1):
9            s = int(a[i]) + int(b[i]) + c
10            res[i] = str(s & 1)
11            c = (s > 1)
12        res = ''.join(res)
13        if c:
14            res = '1' + res
15        return res 