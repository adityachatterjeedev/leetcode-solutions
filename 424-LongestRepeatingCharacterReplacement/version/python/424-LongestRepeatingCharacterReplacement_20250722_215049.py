# Last updated: 7/22/2025, 9:50:49 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counts = {}
        maxf = 0
        for right, letter in enumerate(s):
            lcount = 1 + counts.get(letter, 0)
            counts[letter] = lcount
            substring_len = right - left + 1
            maxf = max(maxf, lcount)
            if substring_len - maxf <= k:
                result = max(result, substring_len)
            else:
                while left<= right:
                    counts[s[left]] -= 1
                    left += 1
                    substring_len -= 1
                    maxf = max(counts.values())
                    if substring_len - maxf <= k:
                        result = max(result, substring_len)
                        break
        return result