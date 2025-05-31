# Last updated: 5/31/2025, 7:04:45 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word.strip() for word in s.split()]
        words.reverse()
        return " ".join(words)