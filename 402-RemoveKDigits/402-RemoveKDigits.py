# Last updated: 7/7/2026, 6:36:24 PM
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        lst = list(num)
        
        stack = []

        for c in lst:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1

            stack.append(c)
        
        stack = stack[:len(stack) - k]

        res = "".join(stack).lstrip('0')
        return res if res else "0"