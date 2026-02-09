# Last updated: 2/8/2026, 10:36:30 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        count = 0
5        left, right = 0, len(people) - 1
6        while left <= right:
7            if people[left] + people[right] > limit:
8                right -= 1
9            else:
10                left += 1
11                right -= 1
12            count += 1
13
14        return count