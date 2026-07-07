# Last updated: 7/7/2026, 6:36:30 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AaEeIiOoUu")

        l, r = 0, len(s) - 1

        lst = list(s)

        while l < r:
            if lst[l] not in vowels:
                l += 1
            elif lst[r] not in vowels:
                r -= 1
            else:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        
        return ''.join(lst)