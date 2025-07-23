# Last updated: 7/22/2025, 10:12:13 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if count[s[r]]> maxf:
                maxf = count[s[r]]
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            if  r - l + 1 > res:
                res = r - l + 1

        return res