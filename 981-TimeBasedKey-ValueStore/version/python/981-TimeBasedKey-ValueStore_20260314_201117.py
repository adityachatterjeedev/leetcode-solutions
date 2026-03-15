# Last updated: 3/14/2026, 8:11:17 PM
1class TimeMap:
2
3    def __init__(self):
4        self.keys = {}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.keys:
8            self.keys[key] = [(timestamp, value)]
9        else:
10            self.keys[key].append((timestamp, value))
11
12    def get(self, key: str, timestamp: int) -> str:
13        if key not in self.keys:
14            return ''
15        if timestamp < self.keys[key][0][0]:
16            return ''
17        elif timestamp > self.keys[key][-1][0]:
18            return self.keys[key][-1][1]
19        else:
20            left ,right = 0, len(self.keys[key])
21            candidate = 0
22            while left <= right:
23                mid = (left + right) // 2
24                if self.keys[key][mid][0] == timestamp:
25                    return self.keys[key][mid][1]
26                elif self.keys[key][mid][0] < timestamp:
27                    candidate = mid
28                    left += 1
29                else:
30                    right -= 1
31            return self.keys[key][candidate][1]
32
33
34# Your TimeMap object will be instantiated and called as such:
35# obj = TimeMap()
36# obj.set(key,value,timestamp)
37# param_2 = obj.get(key,timestamp)