# Last updated: 2/6/2026, 4:08:51 PM
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest = 1
        string = s[0]

        for i in range(1, len(s)):
            if ord(s[i]) - 1 == ord(string[-1]):
                string += s[i]
                longest = max(longest, len(string))
            else:
                string = s[i]
        return longest
