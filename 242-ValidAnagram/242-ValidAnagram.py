# Last updated: 6/16/2025, 3:22:35 PM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)