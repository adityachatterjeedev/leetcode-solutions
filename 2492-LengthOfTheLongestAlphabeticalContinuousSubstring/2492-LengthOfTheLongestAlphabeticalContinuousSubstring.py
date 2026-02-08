# Last updated: 2/8/2026, 3:49:15 AM
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        max_len = curr_len = 1
        prev = ord(s[0])

        for i in range(1, n):
            o = ord(s[i])
            if o == prev + 1:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            else:
                curr_len = 1
            prev = o

        return max_len