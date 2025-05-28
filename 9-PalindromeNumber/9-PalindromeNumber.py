# Last updated: 5/28/2025, 4:43:03 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (but not 0 itself) are not palindromes
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10