# Last updated: 7/7/2026, 6:36:27 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        pt = 0
        
        for letter in s:
            while pt < len(t) and t[pt] != letter:
                pt += 1
            
            if pt == len(t):
                return False
            
            pt += 1
        
        return True