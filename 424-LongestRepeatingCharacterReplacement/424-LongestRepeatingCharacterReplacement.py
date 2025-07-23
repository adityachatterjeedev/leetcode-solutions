# Last updated: 7/22/2025, 8:49:55 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counts = {}
        for right, letter in enumerate(s):
            counts[letter] = 1 + counts.get(letter, 0)
            max_count = 0
            for _, lettercount in counts.items():
                max_count = max(max_count, lettercount)

            substring_len = right - left + 1
            if substring_len - max_count <= k:
                result = max(result, substring_len)
            else:
                while left<= right:
                    counts[s[left]] -= 1
                    left += 1
                    substring_len -= 1
                    max_count = 0
                    for _, lettercount in counts.items():
                        max_count = max(max_count, lettercount)
                    if substring_len - max_count <= k:
                        result = max(result, substring_len)
                        break

        return result