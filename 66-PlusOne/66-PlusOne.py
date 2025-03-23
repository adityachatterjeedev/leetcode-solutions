# Last updated: 3/22/2025, 11:29:27 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range( len(digits) - 1, -1, -1):

            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits

            else:
                digits[i] += 1
                break
        return digits