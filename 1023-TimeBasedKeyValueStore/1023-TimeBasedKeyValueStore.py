# Last updated: 7/7/2026, 6:36:04 PM
class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = [(timestamp, value)]
        else:
            self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ''
        if timestamp < self.keys[key][0][0]:
            return ''
        elif timestamp > self.keys[key][-1][0]:
            return self.keys[key][-1][1]
        else:
            left ,right = 0, len(self.keys[key])
            candidate = 0
            while left <= right:
                mid = (left + right) // 2
                if self.keys[key][mid][0] == timestamp:
                    return self.keys[key][mid][1]
                elif self.keys[key][mid][0] < timestamp:
                    candidate = mid
                    left += 1
                else:
                    right -= 1
            return self.keys[key][candidate][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)