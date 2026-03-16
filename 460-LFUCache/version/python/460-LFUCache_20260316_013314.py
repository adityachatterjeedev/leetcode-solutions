# Last updated: 3/16/2026, 1:33:14 AM
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
11        del self.freq_to_keys[freq][key]
12        if not self.freq_to_keys[freq]:
13            del self.freq_to_keys[freq]
14            if freq == self.min_freq:
15                self.min_freq += 1
16        # Add to new frequency
17        freq += 1
18        self.freq_to_keys[freq][key] = None
19        self.key_to_val_freq[key] = (val, freq)
20
21    def get(self, key: int) -> int:
22        if key not in self.key_to_val_freq:
23            return -1
24        self._update_freq(key)
25        return self.key_to_val_freq[key][0]
26
27    def put(self, key: int, value: int) -> None:
28        if self.capacity == 0:
29            return
30        if key in self.key_to_val_freq:
31            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
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