# Last updated: 6/16/2025, 3:22:56 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x/2
        precision = 1e-1
        
        while abs(x - r * r) > precision:
            r = (r + x / r) / 2
            
        return int(r)