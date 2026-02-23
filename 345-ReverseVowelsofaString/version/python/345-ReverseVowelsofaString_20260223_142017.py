# Last updated: 2/23/2026, 2:20:17 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = set("AaEeIiOoUu")
4
5        l, r = 0, len(s) - 1
6
7        lst = list(s)
8
9        while l < r:
10            if lst[l] not in vowels:
11                l += 1
12            elif lst[r] not in vowels:
13                r -= 1
14            else:
15                lst[l], lst[r] = lst[r], lst[l]
16                l += 1
17                r -= 1
18        
19        return ''.join(lst)