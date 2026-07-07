# Last updated: 7/7/2026, 6:36:21 PM
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}                  # key -> (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys in LRU order

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]
        # Remove from old frequency
        self.freq_to_keys[freq].pop(key)
        # Update min_freq if needed
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1
        # Add to new frequency
        freq += 1
        self.freq_to_keys[freq][key] = None
        self.key_to_val_freq[key] = (val, freq)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            val, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._update_freq(key)
            return
        if len(self.key_to_val_freq) >= self.capacity:
            # Evict LRU key from min frequency
            lru_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[lru_key]
        # Insert new key with frequency 1
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)