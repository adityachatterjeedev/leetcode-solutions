# Last updated: 3/24/2025, 10:50:25 AM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count =  0
        exp = 0
        i = len(columnTitle) - 1
        while i >= 0:
            count += (ord(columnTitle[i]) - 64) * (26 ** exp)
            i -= 1
            exp += 1
        return count
