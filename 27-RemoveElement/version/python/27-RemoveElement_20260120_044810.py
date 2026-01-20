# Last updated: 1/20/2026, 4:48:10 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        if not nums: return 0
4        left, right = 0, len(nums) - 1
5        while nums[right] == val:
6                right -= 1
7                if right == -1:
8                    return 0
9        while left < right:
10            if nums[left] == val:
11                nums[left], nums[right] = nums[right], nums[left]
12            left += 1
13            while nums[right] == val:
14                    right -= 1
15        return right + 1 
16        