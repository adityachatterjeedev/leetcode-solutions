# Last updated: 7/7/2026, 6:36:08 PM
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.capacity = k
        self.size = 0
        self.head = -1

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.head = (self.head + 1) % self.capacity
        self.q[self.head] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        tail = (self.head - self.size + 1) % self.capacity
        return self.q[tail]

    def Rear(self) -> int:
        return -1 if self.size == 0 else self.q[self.head]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()