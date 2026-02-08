# Last updated: 2/8/2026, 3:49:31 AM
class MyQueue:

    def __init__(self):

        self.pushstack = []
        self.popstack = []


    def push(self, x: int) -> None:
        self.pushstack.append(x)

    def pop(self) -> int:
        if self.popstack:
            return self.popstack.pop()
        else:
            for _ in range(len(self.pushstack) - 1):
                self.popstack.append(self.pushstack.pop())
            return self.pushstack.pop()

    def peek(self) -> int:
        if self.popstack:
            return self.popstack[-1]
        else:
            return self.pushstack[0]

    def empty(self) -> bool:
        return (len(self.pushstack) + len(self.popstack)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()