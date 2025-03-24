# Last updated: 3/24/2025, 10:54:41 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[n - i]
            s[n - i] = temp