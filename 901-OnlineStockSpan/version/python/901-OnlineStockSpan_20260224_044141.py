# Last updated: 2/24/2026, 4:41:41 AM
class StockSpanner:

    def __init__(self):
        self.monotonic = []  # monotonically decreasing stack.

    def next(self, price: int) -> int:
        span = 1
        while self.monotonic and self.monotonic[-1][0] <= price:
            span += self.monotonic.pop()[1]

        self.monotonic.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)