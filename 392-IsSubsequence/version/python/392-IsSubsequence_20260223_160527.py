# Last updated: 2/23/2026, 4:05:27 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        if not s:
4            return True
5        
6        pt = 0
7        
8        for letter in s:
9            while pt < len(t) and t[pt] != letter:
10                pt += 1
11            
12            if pt == len(t):
13                return False
14            
15            pt += 1
16        
17        return True