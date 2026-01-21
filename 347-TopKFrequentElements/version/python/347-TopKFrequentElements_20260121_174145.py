# Last updated: 1/21/2026, 5:41:45 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        counts = Counter(nums)
4
5        rev_counts = defaultdict(list)
6        for key,value in counts.items():
7            rev_counts[value].append(key)
8        result = []
9        for i in range(len(nums), 0, -1):
10            
11            if i in rev_counts:
12                result += rev_counts[i]
13                if len(result) > k:
14                    return result[:k]
15
16        return result