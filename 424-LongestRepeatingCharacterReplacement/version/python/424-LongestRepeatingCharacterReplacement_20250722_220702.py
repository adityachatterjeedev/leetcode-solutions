# Last updated: 7/22/2025, 10:07:02 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counts = {}
        maxf = 0
        for right, letter in enumerate(s):
            lettercount = 1 + counts.get(letter, 0)
            counts[letter] = lettercount
            maxf = max(maxf, lettercount)
            substring_len  = right - left + 1
            while substring_len - maxf > k:
                counts[s[left]] -= 1
                left += 1
                substring_len -= 1
            result = max(result, substring_len)

        return result