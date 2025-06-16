# Last updated: 6/16/2025, 3:22:26 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                first = s[l:r]
                second = s[l + 1: r + 1]
                return first == first[::-1] or second == second[::-1]
            l += 1
            r -= 1

        return True