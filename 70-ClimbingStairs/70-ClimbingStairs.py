# Last updated: 3/22/2025, 11:37:51 PM
fib_dict = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2,3]:
            return n
        elif n in fib_dict:
            return fib_dict[n]
        else:
            sol = self.climbStairs(n - 1) + self.climbStairs (n - 2)
            fib_dict[n] = sol
            return sol