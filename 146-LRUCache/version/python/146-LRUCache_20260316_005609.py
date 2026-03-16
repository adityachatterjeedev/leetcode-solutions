# Last updated: 3/16/2026, 12:56:09 AM
1class LRUCache:
2
3    def __init__(self, capacity: int):
4        self.capacity = capacity
5        self.cache = OrderedDict()
6
7    def get(self, key: int) -> int:
8        if key not in self.cache:
9            return -1
10        self.cache.move_to_end(key)
11        return self.cache[key]
12
13    def put(self, key: int, value: int) -> None:
14        self.cache[key] = value
15        self.cache.move_to_end(key)
16        
17        if len(self.cache) > self.capacity:
18            self.cache.popitem(last = False)
19