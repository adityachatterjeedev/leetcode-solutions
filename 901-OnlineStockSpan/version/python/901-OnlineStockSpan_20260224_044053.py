# Last updated: 2/24/2026, 4:40:53 AM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5
6    def next(self, price: int) -> int:
7        total = 1
8        while self.stack and self.stack[-1][0] <= price:
9            _, topDays = self.stack.pop()
10            total += topDays
11        self.stack.append((price, total))
12        return total
13        
14
15
16# Your StockSpanner object will be instantiated and called as such:
17# obj = StockSpanner()
18# param_1 = obj.next(price)