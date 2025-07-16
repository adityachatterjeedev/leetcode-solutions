# Last updated: 7/16/2025, 2:08:02 AM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left, right = 0, len(people) - 1
        while people[right] == limit:
            count += 1
            right -= 1
            if right == -1:
                return count
        
        while left <= right:
            weight = people[left] + people[right]
            if weight > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            count += 1

        return count