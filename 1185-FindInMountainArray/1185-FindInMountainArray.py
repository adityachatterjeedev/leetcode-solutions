# Last updated: 7/7/2026, 6:36:02 PM
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        cache = {}
        
        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        
        n = mountainArr.length()
        
        # 1. Find peak
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if get(mid) < get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        
        # 2. Binary search left (ascending)
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            val = get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # 3. Binary search right (descending)
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = get(mid)
            if val == target:
                return mid
            elif val > target:  # reversed comparison
                l = mid + 1
            else:
                r = mid - 1
        
        return -1  