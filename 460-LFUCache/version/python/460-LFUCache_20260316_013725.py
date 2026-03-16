# Last updated: 3/16/2026, 1:37:25 AM
1class LFUCache:
2    def __init__(self, capacity: int):
3        self.capacity = capacity
4        self.min_freq = 0
5        self.key_to_val_freq = {}                  # key -> (value, freq)
6        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys in LRU order
7
8    def _update_freq(self, key):
9        val, freq = self.key_to_val_freq[key]
10        # Remove from old frequency
11        self.freq_to_keys[freq].pop(key)
12        # Update min_freq if needed
13        if freq == self.min_freq and not self.freq_to_keys[freq]:
14            self.min_freq += 1
15        # Add to new frequency
16        freq += 1
17        self.freq_to_keys[freq][key] = None
18        self.key_to_val_freq[key] = (val, freq)
19
20    def get(self, key: int) -> int:
21        if key not in self.key_to_val_freq:
22            return -1
23        self._update_freq(key)
24        return self.key_to_val_freq[key][0]
25
26    def put(self, key: int, value: int) -> None:
27        if self.capacity == 0:
28            return
29        if key in self.key_to_val_freq:
30            val, freq = self.key_to_val_freq[key]
31            self.key_to_val_freq[key] = (value, freq)
32            self._update_freq(key)
33            return
34        if len(self.key_to_val_freq) >= self.capacity:
35            # Evict LRU key from min frequency
36            lru_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
37            del self.key_to_val_freq[lru_key]
38        # Insert new key with frequency 1
39        self.key_to_val_freq[key] = (value, 1)
40        self.freq_to_keys[1][key] = None
41        self.min_freq = 1
42
43# Your LFUCache object will be instantiated and called as such:
44# obj = LFUCache(capacity)
45# param_1 = obj.get(key)
46# obj.put(key,value)