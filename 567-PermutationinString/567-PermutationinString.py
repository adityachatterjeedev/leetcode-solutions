# Last updated: 6/30/2025, 8:28:11 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        counts1 = {}
        for letter in s1:
            counts1[letter] = 1 + counts1.get(letter, 0)

        left, right = 0, l1 - 1
        counts2 = {}
        for i in range(l1):
            letter = s2[i]
            counts2[letter] = 1 + counts2.get(letter, 0)

        while right < l2 - 1:
            if counts2 == counts1:
                return True
            #remove left
            left_letter = s2[left]
            counts2[left_letter] -= 1
            if counts2[left_letter] == 0:
                del(counts2[left_letter])
            left += 1

            #add right
            right += 1
            right_letter = s2[right]
            counts2[right_letter] = 1 + counts2.get(right_letter, 0)

        if counts2 == counts1:
            return True

        return False