# Last updated: 5/28/2025, 4:45:19 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = [x.strip() for x in s.split()]
        return len(l[-1])