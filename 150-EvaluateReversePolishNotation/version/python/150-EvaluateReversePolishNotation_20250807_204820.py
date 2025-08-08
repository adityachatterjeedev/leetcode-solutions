# Last updated: 8/7/2025, 8:48:20 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opstack = []
        ops = {'+', '-', '*', '/'} 
        for token in tokens:
            if token in ops:
                op1 = opstack.pop()
                op2 = opstack.pop()
                if token == '+':
                    opstack.append(op1 + op2)
                elif token == '-':
                    opstack.append(op2 - op1)
                elif token == '*':
                    opstack.append(op1 * op2)
                else:
                    opstack.append(int(op2 / op1))
            else:
                opstack.append(int(token))
        return opstack[0]