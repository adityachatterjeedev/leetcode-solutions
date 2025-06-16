# Last updated: 6/16/2025, 3:22:24 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        length = len(people)
        people.sort()
        boat_count = 0
        l, r = 0, length - 1
        while l <= r: #fact, people[l] <= limit
            weight_sum = people[l] + people[r]
            if weight_sum <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boat_count += 1

        return boat_count