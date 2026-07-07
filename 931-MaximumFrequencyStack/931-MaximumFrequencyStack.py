# Last updated: 7/7/2026, 6:36:06 PM
class FreqStack:

    def __init__(self):
        self.counts = {} # counts of each value in the stack
        self.max_count = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        val_count = 1 + self.counts.get(val, 0)
        self.counts[val] = val_count
        if val_count > self.max_count:
            self.max_count = val_count
        
        if val_count in self.stacks:
            self.stacks[val_count].append(val)
        else:
            self.stacks[val_count] = [val]

    def pop(self) -> int:
        popped_val = self.stacks[self.max_count].pop()
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        self.counts[popped_val] -= 1
        return popped_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()