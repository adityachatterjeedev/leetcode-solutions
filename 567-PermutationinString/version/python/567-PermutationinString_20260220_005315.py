# Last updated: 2/20/2026, 12:53:15 AM
1from collections import Counter
2class Solution:
3    def checkInclusion(self, s1: str, s2: str) -> bool:
4        if len(s2) < len(s1):
5            return False
6        
7        l1 = len(s1)
8        l2 = len(s2)
9        
10        c1 = Counter(s1)
11
12        c2 = Counter(s2[:l1])
13        if c1 == c2:
14            return True
15
16        left, right = 0, l1-1
17
18        while right < l2 - 1:
19            c2[s2[left]] -= 1
20            left += 1
21            
22            right += 1
23            c2[s2[right]] += 1
24            if c1 == c2:
25                return True
26
27        return False