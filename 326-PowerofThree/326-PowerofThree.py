# Last updated: 3/24/2025, 10:54:11 AM
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