# Last updated: 6/16/2025, 3:22:58 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = [x.strip() for x in s.split()]
        return len(l[-1])