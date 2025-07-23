# Last updated: 7/22/2025, 8:52:56 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counts = {}
        for right, letter in enumerate(s):
            counts[letter] = 1 + counts.get(letter, 0)
            substring_len = right - left + 1
            if substring_len - max(counts.values()) <= k:
                result = max(result, substring_len)
            else:
                while left<= right:
                    counts[s[left]] -= 1
                    left += 1
                    substring_len -= 1

                    if substring_len - max(counts.values()) <= k:
                        result = max(result, substring_len)
                        break

        return result