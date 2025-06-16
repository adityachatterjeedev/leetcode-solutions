# Last updated: 6/16/2025, 3:22:45 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word.strip() for word in s.split()]
        words.reverse()
        return " ".join(words)