# Last updated: 3/8/2026, 12:29:12 AM
1class FreqStack:
2
3    def __init__(self):
4        self.counts = {} # counts of each value in the stack
5        self.max_count = 0
6        self.stacks = {}
7        
8
9    def push(self, val: int) -> None:
10        val_count = 1 + self.counts.get(val, 0)
11        self.counts[val] = val_count
12        if val_count > self.max_count:
13            self.max_count = val_count
14        
15        if val_count in self.stacks:
16            self.stacks[val_count].append(val)
17        else:
18            self.stacks[val_count] = [val]
19
20    def pop(self) -> int:
21        popped_val = self.stacks[self.max_count].pop()
22        if not self.stacks[self.max_count]:
23            self.max_count -= 1
24        self.counts[popped_val] -= 1
25        return popped_val
26
27
28# Your FreqStack object will be instantiated and called as such:
29# obj = FreqStack()
30# obj.push(val)
31# param_2 = obj.pop()