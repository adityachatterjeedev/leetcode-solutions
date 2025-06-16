# Last updated: 6/16/2025, 3:22:33 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref = [0] * len(nums)

        #set prefixes
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            self.pref[i] = prefix


    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right] - (self.pref[left-1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)