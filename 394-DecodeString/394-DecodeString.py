# Last updated: 7/7/2026, 6:36:26 PM
class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []

        curr = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = (10 * k) + int(c)
            elif c == '[':
                string_stack.append(curr)
                count_stack.append(k)
                curr = ''
                k = 0
            elif c == ']':
                curr = (count_stack.pop()) * curr
                curr = string_stack.pop() + curr
            else:
                curr += c

        return curr