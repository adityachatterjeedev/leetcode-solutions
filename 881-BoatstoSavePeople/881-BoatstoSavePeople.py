# Last updated: 7/16/2025, 2:10:19 AM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        left = 0
        right = len(people) - 1
        people.sort()

        while left <= right:
            
            if people[left] + people[right] <= limit:
                # include also the lightest person, ie increment i
                
                left += 1
            # put the heaviest person on the boat
            right -= 1
            ans += 1

        return ans