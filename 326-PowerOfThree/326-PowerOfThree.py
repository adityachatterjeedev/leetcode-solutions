# Last updated: 6/16/2025, 3:22:32 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        
        temp = 1
        while temp < n:
            temp *= 3
            if temp == n:
                return True

        return False