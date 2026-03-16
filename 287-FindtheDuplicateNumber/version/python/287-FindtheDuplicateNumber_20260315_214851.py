# Last updated: 3/15/2026, 9:48:51 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        slow = nums[0]
4        fast = nums[nums[0]]
5        while slow != fast:
6            slow = nums[slow]
7            fast = nums[nums[fast]]
8        
9        slow = 0
10        while slow != fast:
11            slow = nums[slow]
12            fast = nums[fast]
13            
14        return slow