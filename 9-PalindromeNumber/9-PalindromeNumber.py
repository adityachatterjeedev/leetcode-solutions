# Last updated: 5/28/2025, 4:34:53 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        #no string conversions
        x_copy = x
        count = 0 # digit count
        while x_copy > 0:
            x_copy = x_copy // 10
            count += 1

        reverse_num = 0
        x_copy = x
        while x_copy > 0:
            least_sig_digit = x_copy % 10
            reverse_num += least_sig_digit * (10 ** (count - 1))
            x_copy = x_copy // 10
            count -= 1

        return reverse_num == x