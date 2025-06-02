# Last updated: 6/2/2025, 2:38:35 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        length = len(s)
        if length in [0,1]:
            return length

        l, r = 0,0
        maxlen = 0
        contents = {s[0]}
        while r < length - 1:
            r += 1
            if s[r] not in contents:
                contents.add(s[r])
                if r == length - 1:
                    maxlen = max(maxlen, len(contents))
            else:
                maxlen = max(maxlen, len(contents))
                letter = s[r]
                while s[l] != letter:
                    contents.remove(s[l])
                    l += 1
                #do this again to remove the dupe from the substring
                l += 1

        return maxlen
