# Last updated: 6/30/2025, 8:28:57 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        left = 0
        for right in range(len(s2)):
            if right - left + 1 > len(s1):
                left += 1
            
            s2_count = Counter(s2[left:right + 1])
            if s1_count == s2_count:
                return True
        
        return False