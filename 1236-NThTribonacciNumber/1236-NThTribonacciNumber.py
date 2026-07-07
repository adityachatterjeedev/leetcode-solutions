# Last updated: 7/7/2026, 6:36:01 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            a_1, a_2, a_3 = 0, 1, 1

            for _ in range(n - 2):
                a_1, a_2, a_3 = a_2, a_3, a_1 + a_2 + a_3

            return a_3