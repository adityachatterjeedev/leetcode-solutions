# Last updated: 3/24/2025, 10:51:12 AM
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = bin(n)[2:]
        bin_str = ('0' * (32 - len(bin_str))) + bin_str
        rev = '0b' + bin_str[::-1]
        return int(rev,2)
