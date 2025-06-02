# Last updated: 6/2/2025, 3:46:35 AM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n - 1
        boat = 0
        while left <= right:
            total_weight = people[left] + people[right]
            if total_weight > limit:
                boat += 1
                right -= 1
            else:
                boat += 1
                left += 1
                right -= 1
        # if left == right:
        #     return boat + 1
        return boat
            