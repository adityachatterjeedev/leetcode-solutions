# Last updated: 6/1/2025, 3:22:02 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #naive:
        def getnth(idx):
            def get(pair):
                return pair[idx]
            return get

        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        res = list(counts.items())
        res.sort(key=getnth(1), reverse=True)
        res = map(getnth(0), res)
        return list(res)[:k]